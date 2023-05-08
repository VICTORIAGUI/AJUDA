nome = 0
senha = 0

while True:
    print("Olá! Seja Bem vindo, escolha o que deseja fazer: ")
    print("1 - Login")
    print("2 - Cadastro")
    print("3 - Sair")
    print("4 - AJUDA")
    menu_inicial = int(input("Digite aqui: "))

    usuarios = [[0,0], [0,0]]
    for l in range(0, 1):
       for c in range(0,1):
        usuarios[0][0] = nome = str(input("Digite seu login: "))
        usuarios[0][1] = senha = int(input("Digite sua senha: "))
        usuarios[1][0] = nome2 = str(input("Digite seu login: "))
        usuarios[1][1] = senha2 = int(input("Digite sua senha: "))

    if menu_inicial == 1:

        if loginEntrar != nome and senhaEntrar != senha:
           print("Não tem cadastro? Cadastre-se.")
           nome
           senha
           print("Usuário cadastrado com sucesso.")
           nome2
           senha2
           print("Usuário cadastrado com sucesso.")
        elif loginEntrar != nome or senhaEntrar != senha:
           print("Login ou senha incorreta.")
        elif loginEntrar == nome and senhaEntrar == senha:
           print("Login efeituado com sucesso.")
        else:
           print("Verifique seus dados.")
