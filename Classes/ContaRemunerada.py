import datetime as dt
from Classes.Conta import Conta
from Classes.Poupanca import Poupanca

class ContaRemunerada(Conta, Poupanca):
    def __init__(self, cliente, numero, saldo, taxa_rendimento):
        Conta.__init__(self, cliente, numero, saldo)
        Poupanca.__init__(self, taxa_rendimento)

    def render(self):
        self.saldo += self.saldo * (self.taxa_rendimento / 30)
        # self.extrato.operacoes.append(('Rendimento', self.saldo, dt.datetime.now()))
        # return f'O rendimento de R${self.saldo} foi aplicado com sucesso!'