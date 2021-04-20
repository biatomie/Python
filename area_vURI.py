a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)
pi = 3.14159
tri = (a * c) / 2
cir = pi * c ** 2
tra = ((a + b) /2) * c
qua = b ** 2
ret = b * a

print("TRIANGULO: %.3f" "\nCIRCULO: %.3f" "\nTRAPEZIO: %.3f" "\nQUADRADO: %.3f" "\nRETANGULO: %.3f" %(tri, cir, tra, qua, ret))
