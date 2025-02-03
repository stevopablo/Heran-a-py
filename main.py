from Classes.Conta import Conta
from Classes.contaEspecial import ContaEspecial
from Classes.Cliente import Cliente
from Classes.ContaRemunerada import ContaRemunerada
cliente1 = Cliente('123.456.789-00', 'João', 'Rua 1, 123')
cliente2 = Cliente('987.654.321-00', 'Maria', 'Rua 2, 456')


conta1 = Conta(cliente1, 1, 1000)
conta2 = Conta(cliente2, 2, 1000)
conta3 = ContaEspecial(cliente2, 3, 1000, 500) #limite de 500

conta1.info()
conta2.info()

conta1.depositar(100)
conta1.sacar(50)
conta1.transfere_para(conta2, 60)

conta2.sacar(500)
conta2.depositar(200)

conta1.gerar_extrato()
conta2.gerar_extrato()

conta3.depositar(800)
conta3.gerar_extrato()
conta3.sacar(2000)