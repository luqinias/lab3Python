#José Lucas Lira Bizil, 12411ECP005, Engenharia de Computação
def recebeLista():
    while True:
        try:
            sequencia = input("Digite uma sequência de números separados por vírgula: ")
            lista = [int(num) for num in sequencia.split(",")]
            return lista
        except ValueError:
            print("Entrada inválida. Somente números inteiros separados por vírgula.")


def escolhas_booleanas(n_elementos):
    possiveis = []
    for p in range(2**n_elementos):
        # binário
        pb = f"{p:b}"
        # completa prefixo com 0s
        pb = "0" * (n_elementos - len(pb)) + pb
        # armazena a sequência binária para True/False
        possiveis.append([c == "1" for c in pb])
    return possiveis

def gerar_subconjuntos(lista):
    n_elementos = len(lista)
    combinacoes = escolhas_booleanas(n_elementos)
    
    subconjuntos = []
    for combinacao in combinacoes:
        subconjunto = [lista[i] for i in range(n_elementos) if combinacao[i]]
        subconjuntos.append(subconjunto)
    
    return subconjuntos

lista_numeros = recebeLista()
subconjuntos = gerar_subconjuntos(lista_numeros)

print(f"Para a lista {lista_numeros}, temos {2**len(lista_numeros)} possibilidades.")
print("Os possíveis subconjuntos são:")
for subconjunto in subconjuntos:
    print(subconjunto)
