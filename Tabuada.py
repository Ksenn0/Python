#tabuada
n = int(input("Digite um número para ver sua tabuada: "))
print("-" * 20)
i = 1
while(i<=10):
    print("{} X {} = {}".format(n, i, n*i))
    i += 1
print("-" * 20)
