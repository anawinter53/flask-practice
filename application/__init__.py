from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://pbxlbhvm:Da9XYnesnSz9hmiYA8hYTGhb6ZEUvjZX@mel.db.elephantsql.com/pbxlbhvm"
app.config['SECRET_KEY'] = '6d96cbe84031ee83ed73ae13b839967a'
db = SQLAlchemy(app)

from application import routes
