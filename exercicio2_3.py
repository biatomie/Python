num = int(input("Digite um número inteiro:"))
dez = (num - num//100 * 100 - num%10)//10

print("O dígito das dezenas é", dez)
