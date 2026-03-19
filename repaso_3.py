while True:
    try:
  
        edad = int(input("ingresa tu edad: "))
        
    except ValueError:
        print("¡Oops! Por favor, ingresa un número entero válido (por ejemplo: 25).")
        continue 
        
   
    if edad >= 18:
        print(f"Tienes {edad} años. ¡Sos mayor de edad!")
    else:
        print(f"Tienes {edad} años. Sos menor de edad.")
    

    continuar = input("\¿Queres verificar otra edad? (Escribi 'no' para salir, o presiona Enter para seguir): ")
    if continuar.lower() == 'no':
        print("Gracias por verificarte")
        break
