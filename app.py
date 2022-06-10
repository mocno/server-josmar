from Flask import Flask
import db

def create_app():
    return Flask(__name__)

def main():
    app = create_app()

    # Requests
    # Aplicativo: josmar-app
    # - pega informações do usuario (ele mesmo)
    # - situação atual das salas
    # - pega informação da chave
    #
    # Armario: e-josmar
    # - recebe atualização dos dados da posição das chaves (na devolução e no uso das chaves)
    # - faz as verificações de usuario (~~)
    #

    @app.route('/user/get', methods=['GET'])
    def get_user():
        user_id = request.args.get('id', None)

        if user_id is None:
            return {
                'error': 'Id esta vazio, adicione um para pesquisa',
                'status': 'error'
            }

        try:
            with db.create_session() as session:
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
        except (SQLAlchemyError, DisconnectionError):
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
        

if __name__ == '__main__':
    main()
