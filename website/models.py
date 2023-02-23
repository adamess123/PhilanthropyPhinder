from . import db, app
from flask import Flask
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, db.ForeignKey('id'), primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    first_name = db.Column(db.String(150), nullable=False)

    @staticmethod
    def get_reset_token(self, expires_sec=1800):
        s = Serializer(app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'id': self.id}).decode('utf-8')

    def verify_reset_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            id = s.loads(token)['id']
        except:
            return None
        return User.query.get(id)
    def __init__(self, email, password):
        self.email = email
        self.password = password

