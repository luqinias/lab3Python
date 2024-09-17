def recebeLista():
    while True:
        try:
            sequencia = input("Digite uma sequência de números separados por vírgula: ")
            lista = [int(num) for num in sequencia.split(",")]
            return lista
        except ValueError:
            print("Entrada inválida. Somente números inteiros separados por vírgula.")

lista_numeros = recebeLista()

def minl(lista_numeros):
    minimo = lista_numeros[0]
    for num in lista_numeros:
        if num < minimo:
            minimo = num
    return minimo

def maxl(lista_numeros):
    maximo = lista_numeros[0]
    for num in lista_numeros:
        if num > maximo:
            maximo = num
    return maximo

minimo = minl(lista_numeros)
maximo = maxl(lista_numeros)

print("")
print("Resultado:")
print(f"Sobre a entrada validada {lista_numeros}, o elemento mínimo é {minimo} e o máximo é {maximo}")