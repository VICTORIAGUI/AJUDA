nome = "admin"
senha = "12345678"

loginEntrar = input(str("Digite seu login: "))
senhaEntrar = input(str("Digite sua senha: "))

if  loginEntrar != nome and senhaEntrar != senha:
    print("Não tem cadastro? Cadastre-se.")
    nome = input("Digite seu login: ")
    senha = input("Digite sua senha: ")
    print("Usuário cadastrado com sucesso.")
elif loginEntrar != nome or senhaEntrar != senha:
    print("Login ou senha incorreta.")
elif loginEntrar == nome and senhaEntrar == senha:
    print("Login efeituado com sucesso.")
else:
    print("Verifique seus dados.")
