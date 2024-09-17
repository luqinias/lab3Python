def recebeLista():
    while True:
        try:
            sequencia = input("Digite uma sequência de números separados por vírgula: ")
            lista = [int(num) for num in sequencia.split(",")]
            return lista
        except ValueError:
            print("Entrada inválida. Somente números inteiros separados por vírgula.")

lista_numeros = recebeLista()

def eh_par(num):
    return num % 2 == 0

def eh_impar(num):
    return num % 2 != 0

def filtro(predicado, lista_numeros):
    lista_filtrada = []
    for num in lista_numeros:
        if predicado(num):
            lista_filtrada.append(num)
    return lista_filtrada

numeros_pares = filtro(eh_par, lista_numeros)
numeros_impares = filtro(eh_impar, lista_numeros)

print("")
print("Resultado:")
print(f"Para a lista {lista_numeros},\nOs pares são: {numeros_pares}\nOs ímpares são: {numeros_impares}")