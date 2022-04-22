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

def maior_primo(n):
    i=n
    while i != 0:
        if éPrimo(i) == i:
            return i
        else:
            i=i-1
        
