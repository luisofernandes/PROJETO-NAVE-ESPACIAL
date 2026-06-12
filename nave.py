## Definir as variáveis
combustivel = 110
tripulantes = []

## Definir funções

def viajar():
    ##Aqui vamos gastar combustível
    global combustivel ## Avisa a funçao que vamos modificar um variáveç externa
    if (len(tripulantes)==0):
        print("Não há tripulantes. Adicione")

        
    elif(combustivel>=30):
        combustivel = combustivel - 30
        print("A nave viajou")
    else:
        print("Você está sem combustivel suficiente. Abasteça!")

    travarMenu()

def abastecer():
    global combustivel
    combustivel = 110
    print("Tanque cheio ⛽")

    travarMenu()

def status_nave():
    print("\n----------- STATUS DA NAVE -----------")
    print(f"Temos {combustivel} de combustivel")
    print(f"Os tripulantes são: {tripulantes}")
    print("------------------------------ \n")

    travarMenu()

def registrarTripulante():
    ##Essa função pergunta o nome do tripulante e adiciona na lista de tripulantes
    novoTripulante = input("Qual o nome do novo tripulante?: ") #Pergunta quem
    tripulantes.append(novoTripulante) #Inserimos o fulaninho
    print("Tripulante inserido com sucesso! 🚀")

    travarMenu()

def tirarTripulante():
    ##Tira o último tripulante
    if len(tripulantes) > 0:
        removido = tripulantes.pop()
        ##print("Não há tripulantes na nave")
        print(f" {removido} foi removido da missão")
    else:
        tripulantes.pop()
        print(f" ninguém a bordo para remover!")

    travarMenu()

##Criar uma função para pausar o código entre as interações do usuário
def travarMenu():
    #Nosso código vai aqui
    input("\nPressione <ENTER> para continuar....")


##Criar um menu

while True: ##esse loop roda para sempre!
    print("\nBem vindo ao menu interativo da nave. Por favor selecione uma opção:")
    print("\n1- Mostrar status da nave | 2- Viajar | 3- Abastecer | 4- Novo tripulante | 5- Sair")
    opcao = input("Escolha: ")
   
    if (opcao == "1"):
        status_nave()
    elif (opcao == "2"):
        viajar()
    elif (opcao == "3"):
        abastecer()
    elif (opcao == "4"):
        registrarTripulante()
    elif (opcao == "5"):
        print("Viagem encerrada!")
        break


# status_nave()
# registrarTripulante()
# registrarTripulante()
# registrarTripulante()
# status_nave()