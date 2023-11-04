import re

class Usuario:
    def __init__(self,nome,idade,senha,email):
        self.nome = nome
        self.idade = idade
        self.senha = senha
        self.email = email

    def criarUsuário(self):
        self.nome = str(input("COLOQUE O NOME: "))
        self.idade = input("COLOQUE A IDADE: ")
        while not self.idade.isdigit() or int(self.idade)<=0:
            print("IDADE INVÁLIDA")
            self.idade = input("COLOQUE A IDADE: ") 
        
        self.email = input("COLOQUE O EMAIL: ") 
        while not re.match(r"[^@]+@[^@]+\.[^@]+",self.email):
            print("EMAIL INVÁLIDO")
            self.email = input("COLOQUE O EMAIL: ")

        self.senha = input("ADICIONE UMA SENHA FORTE: ")
        while not len(self.senha) >=5:
            print("SUA SENHA DEVE TER MAIS DE 5 CARACTERES")
            self.senha = input("ADICIONE UMA SENHA FORTE: ")