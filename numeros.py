# Programação Orientada a Objetos
# AC01 ADS-EaD - Números especiais
#
# Email Impacta: bianca.yabiku@aluno.faculdadeimpacta.com.br


def eh_primo(n):
    num_divisores = 0 #conta o número de divisores do n
    candidato = 1 #número candidato a divisor
    while candidato <= n:
        if n % candidato == 0:
            num_divisores += 1
        candidato += 1
    if num_divisores == 2:
        return True
    else:
        return False
    # pass


def lista_primos(n):
    primos_encontrados = [] #comeca como uma lista vazia
    for i in range(2,n): #varia i de 1 ate n-1
        if eh_primo(i):
            primos_encontrados.append(i)
    return primos_encontrados 

def conta_primos(s):
    contar_nprimos = {}
    for i in s: # i= número testado s=lista teste
        if eh_primo(i):
            contar_nprimos[i] = s.count(i)
    return contar_nprimos

def eh_armstrong(n):

    if n >= 0:
        nsep = list(map(int,str(n)))
        exp = len(nsep)
        narm = sum(map(lambda x: x ** exp, nsep))
    return n == narm
    
def eh_quase_armstrong(n):

    if n >= 0 and eh_armstrong(n) == False:

        nsep = list(map(int,str(n)))
        exp = len(nsep)
        arm = sum(map(lambda x: x ** exp, nsep))
        qarm = arm-1
    return n == qarm


def lista_armstrong(n):
    """Função que lista os números e Armstrong até n

    Recebe um número natural n e retorna uma lista com todos o
    números de Armstrong estritamente menores que n, em ordem crescente.

    Parâmetros
    ----------
    n : int
        Número natural que define o limite superior da lista.

    Retorno
    -------
    list
        itens : int
        descrição : Uma lista contendo todos os números de Armstrong
            menores que n, em ordem crescente.
    """
    pass


def eh_perfeito(n):
    """Função que verifica se um número é dito perfeito

    Recebe um número natural n, com n >= 2, e retorna verdadeiro se
    n é dito um número perfeito e falso caso contrário

    Exemplos
    --------
    Um número é dito perfeito se a soma de todos os divisores próprios é
    igual a ele mesmo.
    6 é um número perfeito:
        divisores próprios de 6: 1, 2, 3
        1 + 2 + 3 = 6
    12 NÃO é um número perfeito:
        divisores próprios de 12: 1, 2, 3, 4, 6
        1 + 2 + 3 + 4 + 6 = 16

    Parâmetros
    ----------
    n : int
        Número natural a ser testado.

    Retorno
    -------
    bool
        True se n for um número perfeito e False caso contrário.
    """
    pass


def lista_perfeitos(n):
    """Função que lista os números ditos perfeitos até n

    Recebe um número natural n, com n >= 2, e retorna uma lista
    com todos os números perfeitos estritamente menores que n,
    em ordem crescente.

    Parâmetros
    ----------
    n : int
        Número natural que define o limite superior da lista.

    Retorno
    -------
    list
        itens : int
        descrição : Uma lista contendo todos os números perfeitos
            menores que n em ordem crescente.
    """
    pass