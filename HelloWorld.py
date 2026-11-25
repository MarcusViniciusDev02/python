usuario = input('Usuário: ')
senha = input('Senha: ')

while True:
    if (usuario == 'marcus' and senha == '123456'):
        print('Uuario e senha corretos\n')
        break
    else:
        print('Usuário incorreto, tente novamente.')
print('Seja bem vindo')