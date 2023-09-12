from login_reg_app.config.mysqlconnection import connectToMySQL

class Login:
    def __init__(self, data):
        self.id = data['id']
        self.email = data['email']
        self.password = data['password']
        self.first_name = data['first_name']

    @classmethod
    def user_exists(cls, email):
        data = {
            'email': email
        }
        query = 'SELECT * FROM users WHERE users.email = %(email)s'
        results = connectToMySQL('user_login').query_db(query, data)
        print(results)
        if len(results) < 1:
            return False
        return cls(results[0])