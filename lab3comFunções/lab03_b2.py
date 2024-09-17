#José Lucas Lira Bizil, 12411ECP005, Engenharia de Computação
def recebeLista():
    while True:
        try:
            sequencia = input("Digite uma sequência de números separados por vírgula: ")
            lista = [int(num) for num in sequencia.split(",")]
            return lista
        except ValueError:
            print("Entrada inválida. Somente números inteiros separados por vírgula.")

def soma(lista):
    return sum(lista)
    

lista_numeros = recebeLista()

print(f"A soma da entrada validada {lista_numeros} é {soma(lista_numeros)}")