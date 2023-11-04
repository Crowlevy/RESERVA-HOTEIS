# RESERVA DE QUARTOS, VALIDAÇÃO DE USUÁRIO E SISTEMA DE AVALIAÇÃO DE UM HOTEL


### Projeto feito em python para simular a lógica de um hotel, ele se baseia em um sistema de validação de usuário e avaliação.

## FEATURES
### Avaliação Usuário
```python
def sistemaAvaliacao(self,avaliacao,usuario):
        self.avaliacoes.append({"avaliacao":int(avaliacao),"usuario":usuario})
        self.calcularMedia()

    def calcularMedia(self):
        somaAval = sum(item["avaliacao"] for item in self.avaliacoes)
        self.media = somaAval/len(self.avaliacoes) if len(self.avaliacoes)>0 else 0
```
### Adicionar Quartos
```python
def adicionarQuarto(self,numero,tipo):
        for quarto in self.quartos:
            if quarto.numero == numero and not quarto.disp:
                quarto.disponibilidade = True
                print("JÁ EXISTE UM QUARTO COM ESSE NÚMERO")
                return
        novoQuarto = self.quartos.append(Quarto(numero,tipo,disponibilidade=True))
        return novoQuarto


```

### Reservar Quartos
```python
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

   
```

## BIBLIOTECA USADA
* re

```bash
$pip install re 
```

## OBRIGADO
#### CASO TENHA ALGUM BUG, POR FAVOR REPORTAR OU ACRESCENTAR UM FORK PARA AJUDAR:)
<img src="aicalica.jpeg" width="60%" margin="auto"><br>