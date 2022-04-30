senha = "2002"
senhaValida = False


while not senhaValida:
    inputSenha = str(input())

    if senha == inputSenha:
        print("Acesso Permitido")
        senhaValida = True
    else:
        print("Senha Invalida")


