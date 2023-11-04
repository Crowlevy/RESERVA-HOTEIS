from sistemaquartos import Quarto

class Hotel:
    def __init__(self):
        self.quartos = []
        self.disp = False

    def mostrarQuartos(self):
        print("LISTA DE QUARTOS")
        for quarto in self.quartos:
            disponibilidade = "DISPONÍVEL" if quarto.disponibilidade == True else "OCUPADO"
            print(f"\nNÚMERO DO QUARTO {quarto.numero}")
            print(f"TIPO DO QUARTO {quarto.tipo}")
            print(f"STATUS DO QUARTO {disponibilidade}\n")

    def adicionarQuarto(self,numero,tipo):
        for quarto in self.quartos:
            if quarto.numero == numero and not quarto.disp:
                quarto.disponibilidade = True
                print("JÁ EXISTE UM QUARTO COM ESSE NÚMERO")
                return
        novoQuarto = self.quartos.append(Quarto(numero,tipo,disponibilidade=True))
        return novoQuarto


    def buscarQuartos(self,numero):
        for quarto in self.quartos:
            if quarto.numero == numero and quarto.disponibilidade:
                return quarto
            return None

    def reservarQuarto(self,numero):
        for quarto in self.quartos:
            if quarto.numero == numero:
                if quarto.disponibilidade:
                    quarto.disponibilidade = False
                print(f"O QUARTO DO NUMERO {numero} FOI RESERVADO")
                return quarto
            else:
                print("ESSE QUARTO ESTÁ OCUPADO")
                return None

   