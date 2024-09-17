def recebeLista():
    while True:
        try:
            sequencia = input("Digite uma sequência de números separados por vírgula: ")
            lista = [int(num) for num in sequencia.split(",")]
            return lista
        except ValueError:
            print("Entrada inválida. Somente números inteiros separados por vírgula.")

lista_numeros = recebeLista()

def sublista_crescente(lista_numeros):
    if not lista_numeros:
        return []
    
    maior_sublista = []
    aux = [lista_numeros[0]] 

    for i in range(1, len(lista_numeros)):
        if lista_numeros[i] > lista_numeros[i - 1]:
            aux.append(lista_numeros[i])
        else:
            if len(aux) > len(maior_sublista):
                maior_sublista = aux
            aux = [lista_numeros[i]] 

    if len(aux) > len(maior_sublista):
        maior_sublista = aux

    return maior_sublista

maior_sublista = sublista_crescente(lista_numeros)

print("")
print("Resultado:")
print(f"Para a lista {lista_numeros},\nA maior sublista crescente encontrada é: {maior_sublista}")