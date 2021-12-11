numero1 = int(input("Introduce un número"))
numero2 = int(input("Introduce otro número"))

if numero1 < numero2: 
    print(numero1, "<=", numero2) 
elif numero1 > numero2: 
    print(numero1, ">=", numero2) 
else: 
    print(numero1, "=", numero2) 

print("la suma de ambos numeros es de: ", numero1 + numero2)