import datetime as dt
from Classes.Extrato import Extrato

class Conta:
    def __init__(self, cliente, numero, saldo):
        self.cliente = cliente
        self.numero = numero
        self.saldo = saldo
        self.extrato = Extrato()

    def depositar(self, valor):
        self.saldo += valor
        self.extrato.operacoes.append(('Depósito', valor, dt.datetime.now()))
        return f'O valor de R${valor} foi depositado com sucesso!'

    def sacar(self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            return True

    def transfere_para(self, destino, valor):
        if self.sacar(valor):
            destino.depositar(valor)
            self.extrato.operacoes.append(('Transferência', valor, dt.datetime.now()))
            return True
        return False

    def info(self):
        print(f"Cliente: {self.cliente.nome} - Conta: {self.numero} - Saldo: {self.saldo}")
    
    def gerar_saldo(self):
        print(f'Saldo atual: ${self.saldo}')

    def gerar_extrato(self):
        self.extrato.gerar_extrato(self)