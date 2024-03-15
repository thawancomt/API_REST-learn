from flask_restful import Resource

from api import db

class Course(Resource):
    def get(self):
        return {'course': 'Python Flask'}