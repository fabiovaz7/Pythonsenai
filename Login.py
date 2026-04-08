print("="*3 + f"🔒 SISTEMA DE ACESSO " + "="*3)

user_cadastrado = input("USUARIO: ")
senha_cadastrada = input("SENHA: ")

print("Cadastro concluído.")

user_novo = input("Digite seu usuario: ")
senha_nova =input("Digite sua senha: ")

if user_novo == user_cadastrado:
    print("Acesso concedido!")
else:
    print("Usuário não encontrado.")

