class Avaliacao:
    def __init__(self):
        self.avaliacoes = []

    def sistemaAvaliacao(self,avaliacao,usuario):
        self.avaliacoes.append({"avaliacao":int(avaliacao),"usuario":usuario})
        self.calcularMedia()

    def calcularMedia(self):
        somaAval = sum(item["avaliacao"] for item in self.avaliacoes)
        self.media = somaAval/len(self.avaliacoes) if len(self.avaliacoes)>0 else 0
        
    def mostrarAvaliacoes(self):
        for item in self.avaliacoes:
            print(f"AVALIAÇÃO {item['avaliacao']}\nUSUARIO {item['usuario']}\n")
    
    def filtrarUsuario(self,usuario):
        for item in self.avaliacoes:
            if item["usuario"] == usuario:
                print(f"AVALIAÇÃO {item['avaliacao']}, USUÁRIO {item['usuario']}")

    def ordernarAvaliacoes(self):
        self.avaliacoes = sorted(self.avaliacoes,key=lambda x:x["avaliacao"],reverse=True)