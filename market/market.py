from flask import Flask , render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config[UPLOADED_PHOTOS_DEST] = 'uploads'
db = SQLAlchemy(app)

 

