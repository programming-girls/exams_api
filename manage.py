import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

application = Flask(__name__)
application.config[''] = ''
application.config[''] = ''
application.config[''] = ''
application.config[''] = ''
application.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
application.config['FLASK_ADMIN_SWATCH'] = 'cerulean'


SECRET_KEY = os.urandom(32)
application.config['SECRET_KEY'] = SECRET_KEY
db = SQLAlchemy(application)
migrate = Migrate(application, db)
