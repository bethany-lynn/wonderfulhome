"""Models for character creation app"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """A user"""

    __tablename__ = "users"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    username = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(40), unique=True)
    
    def __repr__(self):
        return f'<User: {self.user_id}, email: {self.email}, username: {self.username}>'



def connect_to_db(flask_app, db_uri="postgresql:///creation", echo=False):
    """seting up a connection to a postgreSQL database using a SQLAlchemy library"""
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")

if __name__ == "__main__":
    from server import app

    connect_to_db(app)