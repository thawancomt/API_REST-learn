from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from .config import *

app = Flask (__name__)
app.config.from_object ('config')

db = SQLAlchemy (app)
migrate = Migrate (app, db)
api = Api (app)

from .views import course_view