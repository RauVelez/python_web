print("here")
def encontrar_parejas(numeros, suma_objetivo):
    parejas = []
    for i in range(len(numeros)):
        for j in range(i + 1, len(numeros)):
            if numeros[i] + numeros[j] == suma_objetivo:
                parejas.append((numeros[i], numeros[j]))
    return parejas
lista_numeros = input("Ingresa una lista de números separados por comas: ")
lista_numeros = [int(n) for n in lista_numeros.split(",")]
suma_objetivo = int(input("Ingresa el número objetivo para la suma: "))
parejas_encontradas = encontrar_parejas(lista_numeros, suma_objetivo)
for pareja in parejas_encontradas:
    print(pareja)