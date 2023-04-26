# each class is a table in the database
from application import app, db
from datetime import datetime

app.app_context().push()

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    date_of_release = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"{self.title}: {self.description}"

    def __init__(self, title, description, date_of_release):
        self.title = title
        self.description = description
        self.date_of_release = date_of_release
