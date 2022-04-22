def éPrimo(k):
    i=1
    div=0
    while i <= k: 
        if k%i == 0:
            div = div+1
        else:
            div   
        i=i+1
    if div <= 2:
        primo=k
    else:
        primo=False

    return(primo)

def n_primos(n):
    i=n
    count=-1
    while i != 0:
        if éPrimo(i) == i:
            count=count+1

        i=i-1
    print(count)
        
