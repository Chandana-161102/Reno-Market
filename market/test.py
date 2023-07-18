from market import app
from market import db
with app.app_context():
    db.create_all()