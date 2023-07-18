from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from  flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__) 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = 'fb27b5e24d7e21386bc90abd'
app.config['UPLOAD_FOLDER'] = 'market/static/images'

ALLOWED_EXTENSIONS = {'pdf','png','jpg','jpeg','gif'}

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login_page"
login_manager.login_message_category = "info"
from market import routes