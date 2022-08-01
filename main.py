import time
import random

print("")
print("Bem vindo(a) Empresa de Segurança - Teste123 eu sou a Katie.")
print("")
nome = input("Digite seu nome: ")
senha = input("Sua senha: ")

if (nome == 'Luquinhas123' and senha == 'senhadoida'):
    print("")
    print("Carregando...")
    print("")
    time.sleep(4)
    print("OK")
    print("")
    print("Ola senhor Pedro o que o senhor deseja?")
    print("")
    a = input("Enviar tropas - a / Procurar Pessoas - b / Sair da Conta - c: ")

    if (a == 'a'):
        print("")
        print("OK")
        print("")
        numero = input("Quantas tropas o senhor deseja enviar? ")
        lugar = input("Para qual lugar o senhor deseja envia-las? ")
        senha2 = input("Digite a senha 2 para concluir a solicitação: ")

        if (senha2 == 'senhadoida2'):
            print("")
            print("Carregando...")
            time.sleep(4)
            print("")
            print(numero, "tropas foram enviadas para", lugar, "com êxito")

        else:
            print("")
            print("Carregando...")
            time.sleep(4)
            print("Senha errada!")

    if (a == 'b'):
        print("")
        print("OK")
        print("")
        nomes = input("Qual o nome o senhor deseja procurar? ")

        cidades = ['Rio de Janeiro', 'New York', 'Madrid', 'Los Angeles', 'Minas Gerais', 'Tókio', 'Cancún']
        def selectRandom(cidades):
            return random.choice(cidades)
        
        anos = ['33', '14', '51', '39', '27', '74', '62']
        def selectRandom(anos):
            return random.choice(anos)

        print("")
        print("Carregando...")
        time.sleep(7)
        print("Existe!!!")
        print("")
        print("Nome:", nomes)
        print("Idade:", selectRandom(anos), "anos")
        print("Está em:", selectRandom(cidades))


    if (a == 'c'):
        print("")
        print("OK, até mais senhor!!!")

else:
    print("")
    print("Carregando...")
    time.sleep(4)
    print("Nome ou senha errados")
