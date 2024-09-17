#José Lucas Lira Bizil, 12411ECP005, Engenharia de Computação
def recebeLista():
    while True:
        try:
            sequencia = input("Digite uma sequência de números separados por vírgula: ")
            lista = [int(num) for num in sequencia.split(",")]
            return lista
        except ValueError:
            print("Entrada inválida. Somente números inteiros separados por vírgula.")


def find(elemento, lista):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    if elemento not in lista:
        return Exception("não encontrado na lista.")

def impressao(elemento, lista):
    if isinstance(find(elemento, lista), int):
        return f"encontrado no índice {find(elemento, lista)}."
    else:
        return find(elemento, lista)

lista_numeros = recebeLista()

elemento = int(input("Informe o elemento a ser encontrado na lista: "))
print(f"Para a lista {lista_numeros}, elemento {elemento} {impressao(elemento, lista_numeros)}")