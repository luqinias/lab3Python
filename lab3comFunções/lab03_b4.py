#José Lucas Lira Bizil, 12411ECP005, Engenharia de Computação
def recebeLista():
    while True:
        try:
            sequencia = input("Digite uma sequência de números separados por vírgula: ")
            lista = [int(num) for num in sequencia.split(",")]
            return lista
        except ValueError:
            print("Entrada inválida. Somente números inteiros separados por vírgula.")


def lista_invertida(lista):
    return list(reversed(lista))

lista_numeros = recebeLista()

print(f"Sobre a entrada validada {lista_numeros}, ao revertê-la temos {lista_invertida(lista_numeros)}")