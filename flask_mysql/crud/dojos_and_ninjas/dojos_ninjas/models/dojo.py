from dojos_ninjas.config.mysqlconnection import connectToMySQL
from dojos_ninjas.models.ninja import Ninja

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.ninjas = []

    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        print(results)
        return results

    @classmethod
    def add_dojo_to_db(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s)"
        print(query)
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)

    @classmethod
    def get_single_dojo(cls, id):
        data = {
            'id': id
        }
        query = "SELECT * FROM dojos JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        dojo = cls(results[0])
        for ninja in results:
            dojo.ninjas.append(Ninja(ninja))
        return dojo