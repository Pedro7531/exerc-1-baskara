import math

def retangulo():
    base = float(input("Informe a base: "))
    altura = float(input("Informe a altura: "))
    print("Área do retângulo: ",base * altura)

def triangulo():
    base = float(input("Informe a base: "))
    altura = float(input("Informe a altura: "))
    print("Área do triângulo: ",(base * altura)/2)

def circulo():
    raio = float(input("Informe o raio: "))
    print("Área do círculo: ",math.pi * (raio ** 2))        

opcao = 1

while opcao:
    print ("(1)-Retângulo")
    print ("(2)-Triângulo")
    print ("(3)-Círculo")
    print ("(0)-Sair")

    opcao = int(input("Informe o número da opção:"))

    if (opcao == 1):
        retangulo()
    if (opcao == 2):
        triangulo()
    if (opcao == 3):
        circulo()
    if(opcao==0):
        print("Obrigado por utilizar o calcula área!")           