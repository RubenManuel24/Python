# valor = 1

# while valor < 10:
    # print(valor)
    # valor += 1

# for item in listName:
  # print(item)

# for item in range(20):
#    print(item)

# for item in range(len(listName)):
#    print(f"Posição: {item+1} - {listName[item]}")
listName = ["Ruben", "Ana", "Pinto", "Pinto", "Paulo", "Marcos", "Manuel", "Ruben", "Ruben", "Manuel", "Ruben", "Pinto", "Francisco", "Maria", "Marcos", "Marcos", "Marcos", "Solange", "Manuel", "Manuel"]

print("---- Busca de nome ----")

name = input("Digite um nome:")  # Remove espaços em branco e converte para minúsculas
print(f"Nome digitado: '{name}'")  # Imprime o nome digitado para verificação

quantyName = 0
for item in listName:
    print(f"Comparando '{name}' com '{item.lower()}'")  # Imprime o nome comparado
    if name == item.lower():
        print("")
    else:
        quantyName += 1
        print(f"Quantidade222: {quantyName}")

print(f"Quantidade: {quantyName}")

if quantyName > 0:
    print(f"Na lista tem {quantyName} pessoas com o nome {name}")
else: 
    print(f"Não tem pessoa com o nome {name}")
