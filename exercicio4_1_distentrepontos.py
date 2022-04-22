import math

x1=float(input("Digite um x1:"))
x2=float(input("Digite um x2:"))
y1=float(input("Digite um y1:"))
y2=float(input("Digite um y2:"))

dxy=math.sqrt(((x1-x2)**2)+((y1-y2)**2))

if dxy>=10:
    print("longe")
else:
    print("perto")
