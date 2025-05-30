num = int(input("Digite um número: "))
print('''Escolha uma base para conversão:
      [1] Binário
      [2] Octal
      [3] Hexadecimal''')

opção = int(input("Escolha: "))
if opção == 1:
    print("{} convertido para Binário é: {}".format(num, bin(num)[2:]))
elif opção == 2:
    print("{} convertido para Binário é: {}".format(num, oct(num)[2:]))
elif opção == 3:
    print("{} convertido para Binário é: {}".format(num, hex(num)[2:]))
else:
    print("Opção inválida!")
