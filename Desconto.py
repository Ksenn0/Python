#Desconto
prod_preco = float(input("Qual o preço do produto(R$)? "))
desconto = prod_preco * (5/100)
print("O produto que custava {}, com desconto de 5% passará a custar {:.2f}R$".format(prod_preco, (prod_preco - desconto)))
