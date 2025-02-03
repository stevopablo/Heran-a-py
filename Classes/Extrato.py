import datetime as dt


class Extrato:
    def __init__(self):
        self.operacoes = []

    def gerar_extrato(self, conta):
        print(f'Extrato da conta {conta.numero}')
        for op in self.operacoes:
            print(f'{op[0]:15s}: {op[1]} em {op[2].strftime("%d/%m/%Y %H:%M:%S")}')

        print(f'Saldo atual: {conta.saldo}')
   