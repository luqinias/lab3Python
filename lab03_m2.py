def recebeLista():
    while True:
        try:
            sequencia = input("Digite uma sequência de números separados por vírgula: ")
            lista = [int(num) for num in sequencia.split(",")]
            return lista
        except ValueError:
            print("Entrada inválida. Somente números inteiros separados por vírgula.")


def soma_acumulada(lista_numeros):
    soma = 0
    lista_acumulada = []
    for num in lista_numeros:
        soma += num
        lista_acumulada.append(soma)
    return lista_acumulada

lista_numeros = recebeLista()
resultado = soma_acumulada(lista_numeros)

print("")
print("Resultado:")
print(f"Para a lista {lista_numeros},\nA lista da soma acumulada é: {resultado}")