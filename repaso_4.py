def pedir_letra(mensaje):
   
    while True:
        letra = input(mensaje).upper() 
        
        if len(letra) == 1 and letra.isalpha():
            return letra 
        else:
            print("Escribi UNA letra del alfabeto (sin números).")


print("--- Verificador de Vocales y Consonantes ---")

while True:

    letra_ingresada = pedir_letra("Ingresa una letra del alfabeto: ")
    
    if letra_ingresada in "AEIOU":
        print(f"-> La letra '{letra_ingresada}' es una VOCAL.")
    else:
        print(f"-> La letra '{letra_ingresada}' es una CONSONANTE.")
        
   
   
