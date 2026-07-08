usuarios = {
    "admin": "1234",
    "nathan": "abcd"
}
def validar_login(usuario, senha):
    if usuario in usuarios and usuarios[usuario] == senha:
        print("Login realizado com sucesso!")
    else:
        print("Usuário ou senha incorretos.")
usuario = input("Usuário: ")
senha = input("Senha: ")
validar_login(usuario, senha)