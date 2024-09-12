import math
a= int(input("Digite a:"))
b= int(input("Digite b:"))
c= int(input("Digite c:"))
 
x=(b**2)-(4*a*c)
 
if x<0 :
        print ("Raiz negativa nao pode ser extraida.")
        exit()
 
else :
    x=math.sqrt(x)
    x1=(-b+x)/(2*a)
    x2=(-b-x)/(2*a)
print ("As raizes da equação são:",x1,x2)