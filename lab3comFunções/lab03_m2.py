#José Lucas Lira Bizil, 12411ECP005, Engenharia de Computação
import numpy as np

def recebeLista():
    while True:
        try:
            sequencia = input("Digite uma sequência de números separados por vírgula: ")
            lista = [int(num) for num in sequencia.split(",")]
            return lista
        except ValueError:
            print("Entrada inválida. Somente números inteiros separados por vírgula.")


def somaAcumulada(lista):
    return np.cumsum(lista)

def formatarComVirgula(lista):
    string_com_virgulas = ','.join(map(str, lista))
    lista_convertida = string_com_virgulas.split(',')
    lista_convertida = list(map(int, lista_convertida))
    return lista_convertida


lista_numeros = recebeLista()
soma_acumulada = somaAcumulada(lista_numeros)

print(f"Para a lista {lista_numeros}, a lista da soma acumulada é: {formatarComVirgula(soma_acumulada)}")