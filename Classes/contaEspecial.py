from Classes.Conta import Conta
import datetime as dt

class ContaEspecial(Conta):

    def __init__(self, cliente, numero, saldo, limite):
        super().__init__(cliente, numero, saldo)
        self.limite = limite

    def sacar(self, valor):
        if (self.saldo + self.limite) < valor:
            print(f'Saldo insuficiente para sacar R${valor} na conta {self.numero}')
            return False
        else:
            self.saldo -= valor
            if(self.saldo < 0):
                self.limite += self.saldo
            self.extrato.operacoes.append(('Saque', valor, dt.datetime.now()))
            return True