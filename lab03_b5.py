def recebeLista():
    while True:
        try:
            sequencia = input("Digite uma sequência de números separados por vírgula: ")
            lista = [int(num) for num in sequencia.split(",")]
            return lista
        except ValueError:
            print("Entrada inválida. Somente números inteiros separados por vírgula.")

lista_numeros = recebeLista()

def busca(elemento, lista_numeros):
    for i, num in enumerate(lista_numeros):
        if num == elemento:
            return i  
    return -1

try:
    elemento = int(input("Digite o número a ser encontrado na lista: "))
except ValueError:
    print("Erro: O valor inserido deve ser um número inteiro.")
    exit()


indice = busca(elemento, lista_numeros)

print("")
print("Resultado:")

if indice != -1:
    print(f"Para a lista {lista_numeros},\nO elemento {elemento} foi encontrado no índice {indice}.")
else:
    print(f"Para a lista {lista_numeros},\nO elemento {elemento} não foi encontrado na lista.")
