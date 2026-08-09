from app.models.usuario import Usuario

class UsuarioFactory:
    @staticmethod
    def crear_usuario(username, password,role):
        user = Usuario(username=username, role=role)
        user.set_password(password)
        return user
