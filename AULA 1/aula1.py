print("==== Criação de uma Conta Bancária ====")

name1 = input("Digite o teu nome: ")
name2 = input("Digite o teu sobrenome: ")
age = int(input("Digite a tua idade: ")) 
genero = input("Digite o teu gênero: ")
country = input("Digite o teu país: ")
sald = float(int(input("Digite o teu deposito inicial: ")))


def info_account():
    return f"==== Informação da tua conta ==== \n\nNome: {name1} {name2}\nIdade: {age}\nGênero: {genero}\nPaís: {country}\nSaldo: {sald}"


def validation_age():

    if(genero == "Masculino" and age >= 18 and age <= 90):
        print(info_account())
    elif(genero == "Femenino" and age >= 18 and age <= 85):    
         print(info_account())
    elif(genero == "Femenino" and age >= 18 and age >= 85):  
        print("Maior de 85 anos somente os Homens!!!")  
    else:  
        print("Dados inválidos, verifica melhor os seus dados!!!")



validation_age()