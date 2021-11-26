from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
# from flask_login import LoginManager


app = Flask(__name__)
# configurtaion to connect to database
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///search.db'
app.config['SECRET_KEY'] = 'c4a7217c10e333af03e92501'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
# login_manager = LoginManager(app)
# login_manager.login_view = "login_page"
# login_manager.login_message_category = "info"
from search import routes