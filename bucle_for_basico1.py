

Elegi = int(input("Ingrese cual de los ejercicios quiere ejecutar del 1 al 6: "))

if Elegi == 1:#Básico: imprime todos los números enteros del 0 al 100.
    for i in range(101):
     print(i)
elif Elegi == 2:#Múltiples de 2: imprime todos los números múltiplos de 2 entre 2 y 500
    for i in range(2, 501, 2):
     print(i)   
elif Elegi == 3:#Contando Vanilla Ice: imprime los números enteros del 1 al 100. Si es divisible por 5 imprime “ice ice” en vez del número. Si es divisible por 10, imprime “baby”
    for i in range(1, 101):
       if i % 10 == 0:
        print("baby")
       elif i % 5 == 0:
        print("ice ice")
       else:
        print(i)
elif Elegi == 4:#Wow. Número gigante a la vista: suma los números pares del 0 al 500,000 e imprime la suma total. (Sorpresa, será un número gigante).
    suma = 0
    for i in range(0, 500001, 2):
        suma += i
    print(suma)
elif Elegi == 5:#Regrésame al 3: imprime los números positivos comenzando desde 2024, en cuenta regresiva de 3 en 3.
    for i in range(2023, 0, -3):
     print(i)


elif Elegi == 6:#Establecer 3 variables:(numInicial,numFinal,multiplo)
    #Comenzando en numinicial y pasando por numFinal,imprime los numeros enteros que sean multiplos de multiplo.
    numInicial = int(input("Ingrese un numero entero inicial: "))
    numFinal = int(input("Ingrese un numero entero final: "))
    multiplo = int(input("Ingrese un numero entero multiplo: "))
    if numInicial < numFinal and multiplo > 0:
        for i in range(numInicial,numFinal + 1):
         if i % multiplo == 0:
            print (i)
    else:
        print("Numeros invalidos")
        
else :
    print("Numero invalido")
