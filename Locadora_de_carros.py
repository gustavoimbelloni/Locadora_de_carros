import os

carros = [
        ("Fiat Mobi", 50),
        ("Renault Kwid", 60),
        ("Citroen C3", 70),
        ("Fiat Argo", 80),
        ("Hyundai HB20", 90),
        ("Renault Stepway", 100),
        ("Chevrolet Onix", 110),
        ("Volkswagen Polo", 120),
        ]

alugados = []

def mostrar_lista_de_carros(lista_de_carros):
        for i, car in enumerate(lista_de_carros):
                print("[{}] {} -- R$ {} /dia.".format(i, car[0], car[1]))


while True:
        os.system("cls")
        print('==========')
        print('Bem Vindo à locadora de carros!')
        print('==========')
        print('O que deseja fazer?')
        print('0 - Mostrar portifólio | 1 - Aluguar um carro | 2 - Devolver um carro')
        op = int(input())

        os.system("cls")
        if op == 0:
                mostrar_lista_de_carros(carros)

        elif op == 1:
                mostrar_lista_de_carros(carros)
                print("======")
                print("Escolha o código do carro:")
                cod_car = int(input())
                print("Por quantos dias você deseja alugar este carro?")
                dias = int(input())
                os.system("cls")

                print("Você escolheu {} por {} dias.".format(carros[cod_car][0], dias))
                print("O aluguel totalizaria R$ {}. Deseja alugar?".format(dias * carros[cod_car][1]))

                print("0 - SIM | 1 - NÃO")
                conf = int(input())
                if conf == 0:
                        print("Parabéns você alugou o {} por {} dias.".format(carros[cod_car][0], dias))
                        alugados.append(carros.pop(cod_car))

        elif op == 2:
                if len(alugados) == 0:
                        print("Não há carros para devolver")
                else:
                        print("Segue a lista de carros alugados. Qual você desejaria devolver?")
                        mostrar_lista_de_carros(alugados)
                        print("")
                        print("Escolha o código do carro que deseja devolver:")
                        cod = int(input())
                        if conf == 0:
                                print("Obrigado por devolver o carro {}".format(alugados[cod][0]))
                                carros.append(alugados.pop(cod))

        print("")
        print("=======")
        print("0 para CONTINUAR | 1 para SAIR")
        if float(input()) == 1:
                break