n=int(input("Digite um número inteiro:"))
i=1
dig=0
while  (n*10//(10**i)) > 0:
    
    dig1 = ((n%10**i)-(n%10**(i-1)))/(10**(i-1))
    i=i+1

    dig = dig + dig1

print(dig)
