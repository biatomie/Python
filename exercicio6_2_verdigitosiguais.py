n=int(input("Digite um número inteiro:"))
i=1
dig=0
tem=0
while  (n*10//(10**i)) > 0:
    
    dig1 = ((n%10**i)-(n%10**(i-1)))/(10**(i-1))
    dig2 = ((n%10**(i+1))-(n%10**(i)))/(10**(i))
    i=i+1

    #print ("1:",dig1, "2:",dig2)

    if dig1 == dig2:
        tem = tem+1
    else:
        tem = tem
    
if tem==0:
    print("não")
else:
    print("sim")

