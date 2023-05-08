cad_user = 0
cad_senha = 0
while True:
    #Tela principal
    print("Olá! Seja Bem vindo, escolha o que deseja fazer: ")
    print("1 - Login")
    print("2 - Cadastro")
    print("3 - Sair")
    print("4 - AJUDA")
    user_digi = int(input("Digite aqui: "))

    # Aqui já é o LOGIN
    if user_digi == 1:
        user = input("\nLogin: ") #\n é caracter de escape, que pula uma linha no terminal
        senha = int(input("Senha: "))
        if user == cad_user and senha == cad_senha:
            print("==BEM VINDO AO SISTEMA!===")
            break
        else:
            print("*Usuário ou senha inválidos*\n")

    # Aqui é o cadastro
    elif user_digi == 2:
        print("\nTela de cadastro:")
        cad_user = input("Crie um login: ")
        cad_senha = int(input("Crie uma senha: "))
        print("Cadastro feito com sucesso!\n")

    #Aqui é para sair
    elif user_digi == 3:
        print("Encerrando...")
        break
    elif user_digi == 4:
        print("TELA DE AJUDA")
    else:
        print("Favor digite um dos 3 números indicados\n")