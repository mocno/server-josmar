"""This script creates a Server API for data control"""

import os
from flask import Flask, request
from sqlalchemy.exc import DisconnectionError
import db

"""Create flask app"""
app = Flask(__name__)

app.config["POSTGRES_URI"] = f"postgresql+psycopg2://{os.environ['DB_USERNAME']}:" \
    f"{os.environ['DB_PASSWORD']}@{os.environ['DB_HOSTNAME']}:{os.environ['DB_PORT']}" \
    f"/{os.environ['DB_DATABASE']}"

@app.route("/")
def index():
    """Index page"""
    return "Hello, World!"

@app.route('/user/get', methods=['GET'])
def get_user():
    user_id = request.args.get('id', None)

    if user_id is None:
        return {
            'error': 'No user id provided',
            'status': 'error'
        }

    try:
        with db.create_session(app.config["POSTGRES_URI"]) as session:
            user = session.filter(db.User.id == user_id).first()

            if user is None:
                return {
                    'error': 'User not found',
                    'status': 'error'
                }

            return {
                'user': dict(user),
                'status': 'ok'
            }
    except DisconnectionError:
        return {
            'error': 'Database connection error',
            'status': 'error'
        }

@app.route('/room/map', methods=['GET'])
def rooms_map():
    pass

@app.route('/key/get', methods=['GET'])
def key_get():
    pass

@app.route('/key/update', methods=['POST'])
def key_update():
    pass
