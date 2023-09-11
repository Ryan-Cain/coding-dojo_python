from flask_app.config.mysqlconnection import connectToMySQL

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']

    @classmethod
    def get_all_users(cls):
        query = "SELECT * FROM users"

        results = connectToMySQL('users_schema').query_db(query)

        users = []
        for user in results:
            users.append(cls(user))
        return users

    @classmethod
    def create_new_user(cls, data):
        query = "INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s)"
        return connectToMySQL('users_schema').query_db(query, data)
    
    @classmethod
    def get_user(cls, id):
        data = {
            'id': id
        }
        query = 'SELECT * FROM users WHERE users.id = %(id)s'
        results = connectToMySQL('users_schema').query_db(query, data)
        return results[0]
    
    @classmethod
    def delete_user(cls, id):
        data = {
            'id': id
        }
        query = 'DELETE FROM users WHERE users.id = %(id)s'

        return connectToMySQL('users_schema').query_db(query, data)
    
    @classmethod
    def edit_user(cls, data):
        
        query = "UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s WHERE users.id = %(id)s"

        return connectToMySQL('users_schema').query_db(query, data)
