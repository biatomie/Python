diasem=input()
qd=int(input())
lisem=['domingo','segunda','terca','quarta','quinta','sexta','sabado']
index = lisem.index(diasem)
if qd==0:
    print(f'chega hoje!')
else:
    entr=(index+qd)%7
    print(f'sera entregue {lisem[entr]}')
    

