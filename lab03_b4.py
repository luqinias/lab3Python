def recebeLista():
    while True:
        try:
            sequencia = input("Digite uma sequência de números separados por vírgula: ")
            lista = [int(num) for num in sequencia.split(",")]
            return lista
        except ValueError:
            print("Entrada inválida. Somente números inteiros separados por vírgula.")

lista_numeros = recebeLista()

def reverter(lista_numeros):
    lista_revertida = []
    for i in range(len(lista_numeros) - 1, -1, -1):
        lista_revertida.append(lista_numeros[i])
    return lista_revertida

lista_invertida = reverter(lista_numeros)

print("")
print("Resultado:")
print(f"Sobre a entrada validada {lista_numeros}, ao revertê-la temos {lista_invertida}")