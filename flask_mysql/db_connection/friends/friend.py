from mysqlconnection import connectToMySQL

class Friend:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.occupation = data['occupation']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM friends'

        results = connectToMySQL('friends').query_db(query)

        friends = []

        for friend in results:
            friends.append(cls(friend))

        return friends
    
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO friends ( first_name , last_name , occupation , created_at, updated_at ) VALUES ( %(first_name)s , %(last_name)s , %(occupation)s , NOW() , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('friends').query_db( query, data )
    
    @classmethod
    def get_friend_by_id(cls, id):
        query = 'SELECT * FROM friends WHERE id = %(id)s'
        data = {
            'id': id
        }

        results = connectToMySQL('friends').query_db(query, data)
        print(results)
        row = results[0]

        return row

    # @classmethod
    # def update_record(cls, data):
    #     pass
        

