from flask import Blueprint
from flask import request

from app import db

from models import Card, User

avito = Blueprint('avito', __name__, template_folder='templates', static_folder='static')


def serialize_card(card):
    return {'id': card.id, 'title': card.title, 'description': card.description, 'user_id': card.user_id, 'created_at': card.created_at.isoformat()}


def serialize_user(user):
    return {'id': user.id, 'username': user.username, 'password_hash': user.password_hash}


@avito.route('cards/', methods=['GET', 'POST'])
def cards():
    if request.method == 'POST':
        c = Card(**request.json)
        db.session.add(c)
        db.session.commit()
        return serialize_card(c)

    else:
        qs = Card.query.all()
        list_result = []

        for x in qs:
            list_result.append(serialize_card(x))
        return list_result


@avito.route('users/', methods=['GET', 'POST'])
def users():
    if request.method == 'POST':
        u = User(**request.json)
        db.session.add(u)
        db.session.commit()
        return serialize_user(u)

    else:
        qs = User.query.all()
        list_result = []

        for x in qs:
            list_result.append(serialize_user(x))
        return list_result




