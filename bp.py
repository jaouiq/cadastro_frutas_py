# lista de frutas
frutas = ['maracujá', 'banana', 'maçã']

# usuário informa o nome da nova fruta
nova_fruta = input('Informe o nome da nova fruta: ')

# nova fruta é inserida na lista
frutas.append(nova_fruta)

# exibe na tela a nova lista
for fruta in frutas:
    print(fruta)