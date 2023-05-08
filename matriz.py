usuarios = [[0,0], [0,0]]

for l in range(0, 1):
    for c in range(0,1):
        usuarios[0][0] = str(input("Digite seu login: ")) 
        usuarios[0][1] = int(input("Digite sua senha: "))
        usuarios[1][0] = str(input("Digite seu login: "))
        usuarios[1][1] = int(input("Digite sua senha: "))
        
print(usuarios)