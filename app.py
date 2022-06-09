from Flask import Flask

def create_app():
    return Flask(__name__)

class JosmarUser():
    def __init__(self, _id: int, name: str, access: int):
        self.id = _id
        self.name = name
        self.access = access
        self.current_keys = []

class JosmarKey():
    def __init__(self, _id: int, name: str, room: JosmarRoom):
        self.id = _id
        self.name = name
        self.room = room

class JosmarRoom():
    def __init__(self, _id: int, name: str):
        self.id = _id
        self.name = name
        self._keys = []

def main():
    app = create_app()

    # Requests
    # Aplicativo: josmar-app
    # - pega informações do usuario (ele mesmo)
    # - situação atual das salas
    # - pega informação das chaves
    #
    # Armario: e-josmar
    # - recebe atualização dos dados da posição das chaves (na devolução e no uso das chaves)
    # - faz as verificações de usuario (~~)
    #

    app.route('/user/', methods=['GET'])
    def get_user():
        return [
            'user'
        ]

    app.route('/user/', methods=['POST'])
    def edit_user():
        return [
            'user'
        ]

if __name__ == '__main__':
    main()
