#José Lucas Lira Bizil, 12411ECP005, Engenharia de Computação
def recebeLista():
    while True:
        try:
            sequencia = input("Digite uma sequência de números separados por vírgula: ")
            lista = [int(num) for num in sequencia.split(",")]
            return lista
        except ValueError:
            print("Entrada inválida. Somente números inteiros separados por vírgula.")

def sublistaCrescente(lista):
    sublista = []
    maior_sublista = []
    for i in range(len(lista)):
        if i == 0 or lista[i] > lista[i-1]:
            sublista.append(lista[i])
        else:
            if len(sublista) > len(maior_sublista):
                maior_sublista = sublista
            sublista = [lista[i]]
    
    if len(sublista) > len(maior_sublista):
        maior_sublista = sublista
    
    return maior_sublista

lista_numeros = recebeLista()

print(f"Para a lista {lista_numeros}, a maior sublista crescente encontrada é: {sublistaCrescente(lista_numeros)}")
