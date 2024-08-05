try: 
    numero = int(input("Digite um número:"))
    print(numero/0) 

except ZeroDivisionError:
     print("Não podemos dividir um número por 0.")
except ValueError:
     print("Digite um valor válido")
except:
     print("Erro inesperado")
finally:
     print("O programa fechou com sucesso!")