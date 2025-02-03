import datetime as dt
from Classes.Conta import Conta

class Poupanca:
    def __init__(self, taxa_rendimento):
        self.taxa_rendimento = taxa_rendimento

    def render(self, conta: Conta):
        conta.saldo += conta.saldo * (self.taxa_rendimento / 30)
        conta.extrato.operacoes.append(('Rendimento', conta.saldo, dt.datetime.now()))
        return f'O rendimento de R${conta.saldo} foi aplicado com sucesso!'