from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def standard_board():
    return render_template('index.html', row=8, col=8, color1='rgb(255, 255, 224)', color2='rgb(85, 107, 47)')

@app.route('/<int:rows>')
def custom_col_board(rows):
    return render_template('index.html', row=rows, col=8, color1='rgb(255, 255, 224)', color2='rgb(85, 107, 47)')

@app.route('/<int:rows>/<int:cols>')
def custom_col_row_board(rows, cols):
    return render_template('index.html', row=rows, col=cols, color1='rgb(255, 255, 224)', color2='rgb(85, 107, 47)')

@app.route('/<int:rows>/<int:cols>/<string:color1>/<string:color2>')
def custom_col_row_colors_board(rows, cols, color1, color2):
    return render_template('index.html', row=rows, col=cols, color1=color1, color2=color2)


if __name__ == "__main__":
    app.run(debug=True)