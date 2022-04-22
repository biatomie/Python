import math

a=float(input("a:"))
b=float(input("b:"))
c=float(input("c:"))
delta=b**2-4*a*c

if delta==0:
      x1=-b/(4*a*c)
      print ("a raiz desta equação é",x1)
if delta>0:
      rdelta=math.sqrt(delta)
      x1=(-b+rdelta)/(4*a*c)
      x2=(-b-rdelta)/(4*a*c)
      if x1>x2:
            print ("as raízes da equação são",x1," e",x2)
      else:
            print ("as raízes da equação são",x2," e",x1)
else:
      print("esta equação não possui raízes reais")
      
