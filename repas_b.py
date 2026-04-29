while True:
    try:            
        numero1 = float(input("Ingresa el primer número: "))
        numero2 = float(input("Ingresa el segundo número: "))

    except ValueError:
        print("ta mal pa flasheaste")
        continue #
        
    # Comparar los números para determinar cuál es el mayor
    if numero1 > numero2:
        print(f"El número más grande es: {numero1}")
    elif numero2 > numero1:
        print(f"El número más grande es: {numero2}")
    else:
        print("Ambos números son exactamente iguales.")
