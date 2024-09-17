#José Lucas Lira Bizil, 12411ECP005, Engenharia de Computação
def recebeLista():
    while True:
        try:
            sequencia = input("Digite uma sequência de números separados por vírgula: ")
            lista = [int(num) for num in sequencia.split(",")]
            return lista
        except ValueError:
            print("Entrada inválida. Somente números inteiros separados por vírgula.")

def minimo(lista):
    return min(lista)

def maximo(lista):
    return max(lista)
    

lista_numeros = recebeLista()

print(f"Sobre a entrada validada {lista_numeros}, o elemento mínimo é {minimo(lista_numeros)} e o máximo é {maximo(lista_numeros)}")