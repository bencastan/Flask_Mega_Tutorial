from app import db

class User(db.Model):
    id = db.Column(db.INteger, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(128), index=True, unique=True)
    password_hash = db.Column(db.string(128))

    def __repr__(self):
        return '<user {}>'.format(self.username)