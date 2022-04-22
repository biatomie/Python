def computador_escolhe_jogada(n,m):

    if n-m == 0:
        m=r
    elif n-m =
    print("O computador tirou uma peça.)
    print("O computador tirou 2 peças.)
        
        

def usuario_escolhe_jogada(n,m):
    print("Voce começa!")
    
def partida():

    i=1
    while (i<4):
        print("**** Rodada",i ,"****")
        i=i+1
        print()
        n=int(input("Quantas peças? "))
        m=int(input("Limite de peças por jogada? "))
        print()


        if n%(m+1)==0:
            print("Computador começa!")
            usuario_escolhe_jogada(n,m)
              
        else:
            print("Voce começa!")
            computador_escolhe_jogada(n,m)

def main():
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print()
    print("1 - para jogar uma partida isolada")
    tipo=int(input("2 - para jogar um campeonato "))
    print()


    if tipo==1:
        print("Voce escolheu uma partida isolada!")
        print()
        partida()
    elif tipo==2:
        print("Voce escolheu um campeonato!")
        print()
        campeonato()
    else:
        print("Valor inválido")
        print()
        main()

main()

