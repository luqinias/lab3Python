lista = input("Digite uma sequência de números separados por vírgula: ")

lista_num = []
item = ""

for char in lista:
    if char == ',':
        try:
            lista_num.append(int(item))
        except ValueError:
            print(f"'{item}' não é um número válido e será ignorado.")
        item = ""
    else:
        item += char

if item:
    try:
        lista_num.append(int(item))
    except ValueError:
        print(f"'{item}' não é um número válido e será ignorado.")

def soma(lista_num):
    soma = 0
    for i in lista_num:
        soma += i
    return soma

soma_lista = soma(lista_num)

print("")
print("Resultado:")
print(f"A soma da entrada validada {lista_num} é {soma_lista}")