#José Lucas Lira Bizil, 12411ECP005, Engenharia de Computação
def recebeLista():
    while True:
        try:
            sequencia = input("Digite uma sequência de números separados por vírgula: ")
            lista = [int(num) for num in sequencia.split(",")]
            return lista
        except ValueError:
            print("Entrada inválida. Somente números inteiros separados por vírgula.")


def par(lista):
    pares = list(filter(lambda x: x % 2 == 0, lista))
    return pares
def impar(lista):
    impares = list(filter(lambda x: x % 2 != 0, lista))
    return impares

def filtro(predicado, lista):    
    return predicado(lista)

lista_numeros = recebeLista()

print(f"Para a lista {lista_numeros}, os pares são: {filtro(par,lista_numeros)} e os ímpares são: {filtro(impar,lista_numeros)}")