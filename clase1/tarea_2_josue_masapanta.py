# ejercicio 2

# Función para pedir los dos números del intervalo
def pedir_intervalo():
    menor = int(input("Ingresa el número menor: "))
    mayor = int(input("Ingresa el número mayor: "))
    return menor, mayor

# Función para verificar si el intervalo es válido
def validar_intervalo(menor, mayor):
    return menor < mayor

# Función que devuelve los números pares del intervalo
def obtener_pares(menor, mayor):
    pares = []
    for num in range(menor, mayor + 1):
        if num % 2 == 0:
            pares.append(num)
    return pares

# Función principal
def ejercicio2(menor, mayor):
    if not validar_intervalo(menor, mayor):
        return "El número menor debe ser menor que el mayor."
    
    pares = obtener_pares(menor, mayor)
    cantidad = mayor - menor + 1

    mensaje = f"\nNúmeros pares entre {menor} y {mayor}:\n"
    mensaje += ", ".join(str(p) for p in pares)
    mensaje += f"\n\nCantidad total de números en el intervalo: {cantidad}"
    return mensaje

# Ejecutar el programa
if __name__ == "__main__":
    menor, mayor = pedir_intervalo()
    resultado = ejercicio2(menor, mayor)
    print(resultado)
