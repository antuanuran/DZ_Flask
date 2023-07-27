from app import db
import datetime as dt


class User(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    cards = db.relationship('Card', backref='owner', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Card(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    title = db.Column(db.String(64), index=True)
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, index=True, default=dt.datetime.utcnow)
    user_id = db.Column(db.BigInteger, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Card {}>'.format(self.title)
