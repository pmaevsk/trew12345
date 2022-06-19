from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSON
from flask_migrate import Migrate
import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
env_path = os.path.join(basedir, '.env')
load_dotenv(env_path)
URL = os.getenv('db_url')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)




class MyForm(db.Model):
    __tablename__ = 'my_form'

    id = db.Column(db.Integer, primary_key=True)
    form = db.Column(JSON)

    def __init__(self, form):
        self.form = form

    def __repr__(self):
        return f"<{self.form}>"

from app.views import form_blueprint

app.register_blueprint(form_blueprint)
