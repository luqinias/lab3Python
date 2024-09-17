def recebeLista():
    while True:
        try:
            sequencia = input("Digite uma sequência de números separados por vírgula: ")
            lista = [int(num) for num in sequencia.split(",")]
            return lista
        except ValueError:
            print("Entrada inválida. Somente números inteiros separados por vírgula.")

def remove_duplicatas(lista):
    lista_unica = []
    for num in lista:
        if num not in lista_unica:
            lista_unica.append(num)
    return lista_unica

lista_numeros = recebeLista()
resultado = remove_duplicatas(lista_numeros)

print("")
print("Resultado:")
print(f"Para a lista {lista_numeros},\nSeus elementos únicos são {resultado}")