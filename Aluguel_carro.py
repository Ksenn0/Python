#aluguel de carro
dias = int(input("O Carro foi alugado por quantos dias? "))
km = float(input("Quantos Km o carro percorreu? "))
valor_a_pagar = (dias * 60) + (km * 0.15)
print("Total a pagar: {:.2f}R$".format(valor_a_pagar))
