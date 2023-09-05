# Create a new Flask project called counter
# Have the root route render a template that displays the number of times the client has visited this site. Refresh the page several times to ensure the counter is working.
# Add a "/destroy_session" route that clears the session and redirects to the root route. Test it.
# NINJA BONUS: Add a +2 button underneath the counter and a new route that will increment the counter by 2
# NINJA BONUS: Add a Reset button to reset the counter
# SENSEI BONUS: Add a form that allows the user to specify the increment of the counter and have the counter increment accordingly
# SENSEI BONUS: Adjust your code to display both how many times the user has actually visited the page, as well as the value of the counter, given the above functionality
# SENSEI BONUS: Decode the cookie information as shown in the video



from flask import Flask, render_template, redirect, request, session
import base64

app = Flask(__name__)
app.secret_key = 'this is the secret'


@app.route('/')
def counter():
    if 'count' in session:
        session['count'] = session['count'] + 1
    else:
        session['count'] = 1
        session['actual_count'] = 0
        session['boosted'] = 0
    if session['boosted'] > 0:
        return redirect('/multiple_visits')
    else:
        session['actual_count'] = session['actual_count'] + 1

    count = '{"count":'
    amount = session['count']
    end = "}'"
    fullString = count+str(amount)+end
    byteString = bytes(fullString, 'utf-8')

    b64_encoded_string = base64.urlsafe_b64encode(byteString)
    b64_encoded_string = b64_encoded_string[:16]
    finalStr = b64_encoded_string.decode('utf-8')
    
    return render_template('index.html', finalStr=finalStr)

@app.route('/two_visits')
def two_visits():
    session['count'] = session['count'] + 1
    session['boosted'] = session['boosted'] - 1
    return redirect('/') 

@app.route('/multiple_visits', methods=['POST', 'GET'])
def multiple_visits():
    if session['boosted'] == 0:
        session['boosted'] = int(request.form['number'])
    if session['boosted'] > 0:
        # session['count'] = session['count'] + 1
        session['boosted'] = session['boosted'] - 1
    return redirect('/') 
    

@app.route('/destroy_session')
def reset():
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)