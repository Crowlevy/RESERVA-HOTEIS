from reservahoteis import Hotel
from avaliacao import Avaliacao
from usuario import Usuario

hotel = Hotel()
avaliacao = Avaliacao()
usuario = Usuario("", 0, "", "")
usuario.criarUsuário()


while True:

    print(f"{'-----SISTEMA DE RESERVA DE QUARTOS-----':^50}")
    print("\nESCOLHA UMA OPÇÃO: ")
    opcoes = ['1-ADICONAR QUARTO','2-BUSCAR QUARTO','3-RESERVAR QUARTO','4-MOSTRAR TODOS OS QUARTOS','5-AVALIAR HOTEL','6-MOSTRAR AVALIAÇÕES USUÁRIOS','0-SAIR']
    for opc in opcoes:
        print(opc)
    escolha = int(input("COLOQUE O QUE DESEJA: "))
    
    if escolha == 1:
        numero = int(input("COLOQUE O NÚMERO DO QUARTO: "))
        tipo = str(input("COLOQUE O TIPO DO QUARTO: "))
        hotel.adicionarQuarto(numero,tipo)
    
    elif escolha == 2:
        numero = int(input("QUAL O NÚMERO DO QUARTO: "))
        hotel.buscarQuartos(numero)

    elif escolha == 3:
        numero = int(input("COLOQUE O NÚMERO DO QUARTO QUE DESEJA RESERVAR: "))
        hotel.reservarQuarto(numero)
    
    elif escolha == 4:
        hotel.mostrarQuartos()
    
    elif escolha == 5:
        avalUser = input("COLOQUE A SUA AVALIAÇÃO DE 0 A 5: ")
        while not avalUser.isdigit() or float(avalUser)<0 or float(avalUser)>5:
            print("INVÁLIDO")
            avalUser = input("COLOQUE A SUA AVALIAÇÃO DE 0 A 5: ")
        avaliacao.sistemaAvaliacao(avalUser,usuario.nome)
        print("AVALIAÇÃO FEITA COM SUCESSO!!")    
    
    elif escolha == 6:
        avalOrdem = avaliacao.ordernarAvaliacoes()
        avaliacao.mostrarAvaliacoes()
    
    elif escolha == 0:
        print("OBRIGADOO,VOLTE SEMPRE!!!")
        break
    