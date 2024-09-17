#José Lucas Lira Bizil, 12411ECP005, Engenharia de Computação
def recebeLista():
    while True:
        try:
            sequencia = input("Digite uma sequência de números separados por vírgula: ")
            lista = [int(num) for num in sequencia.split(",")]
            return lista
        except ValueError:
            print("Entrada inválida. Somente números inteiros separados por vírgula.")

def tamanho(lista):
    return len(lista)

lista_numeros = recebeLista()

print(f"A entrada validada {lista_numeros} tem {tamanho(lista_numeros)} elementos.")