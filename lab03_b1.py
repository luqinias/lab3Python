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

# Adicionar o último item após o loop
if item:
    try:
        lista_num.append(int(item))
    except ValueError:
        print(f"'{item}' não é um número válido e será ignorado.")

def tamanho(lista_num):
    count = 0
    for _ in lista_num:
        count += 1
    return count

tamanho_lista = tamanho(lista_num)

print("")
print("Resultado:")
print(f"A entrada validada {lista_num} tem {tamanho_lista} elementos.")