from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# create flask app
app = Flask(__name__)
app.config["SECRET_KEY"] = "secret-key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db" #URI for SQLite library

db = SQLAlchemy(app) 
# db.app = app # try this line, should remove it

from routes import * # this line should be below the app creation line

if __name__ == '__main__':
    app.run(debug=True)