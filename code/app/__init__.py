"""This script creates a Server API for data control"""

import os
from flask import Flask, request
from sqlalchemy.exc import DisconnectionError
import db

def create_app():
    """Create flask app"""
    app = Flask(__name__)

    app.config["POSTGRES_URI"] = f"postgresql+psycopg2://{os.environ['DB_USERNAME']}:" \
        f"{os.environ['DB_PASSWORD']}@{os.environ['DB_HOSTNAME']}:{os.environ['DB_PORT']}" \
        f"/{os.environ['DB_DATABASE']}"

    return app

def start_app():
    """Start flask app with api routes"""

    app = create_app()

    @app.route('/user/get', methods=['GET'])
    def get_user():
        user_id = request.args.get('id', None)

        if user_id is None:
            return {
                'error': 'Id esta vazio, adicione um para pesquisa',
                'status': 'error'
            }

        try:
            with db.create_session(app.config["POSTGRES_URI"]) as session:
                user = session.filter(db.User.id == user_id).first()

                if user is None:
                    return {
                        'error': 'Usuário não foi encontrado, foi morto',
                        'status': 'error'
                    }

                return {
                    'user': dict(user),
                    'status': 'ok'
                }
        except DisconnectionError:
            return {
                'error': 'Error interno, erro de conexão do banco de dados',
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

    environment_debug = os.environ.get("APP_DEBUG", "False") == "True"
    environment_port = os.environ.get("APP_PORT", 5000)
    app.run(host='0.0.0.0', port=environment_port, debug=environment_debug)

if __name__ == '__main__':
    start_app()
