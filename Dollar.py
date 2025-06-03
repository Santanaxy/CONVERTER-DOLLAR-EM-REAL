
def converter_real():
    converter = float(input("DIGITE O VALOR EM DOLLAR: "))
   
    dollar = converter / 5.64 

    real =  converter * 5.64 
    print("--------------------------------------------------")
    print(f"{dollar}USD equivalente a R${real: .2f}R$")



def converter_dollar():
    
    converter2 = float(input("DIGITE O VALOR EM REAL: "))

    real =  converter2 * 5.64 

    dollar = converter2 / 5.64 


    print(f"{real}BRL equivalente a US$ {dollar: .2f}") 

def menu ():
    while True:
        print("\n CONVERSOR DE MOEDAS")
        print("[1] CONVERTER EM DOLLAR PARA REAL")
        print("[2] CONVERTER REAL PARA DOLLAR")
        print("[0] SAIR")
        opcao = input("ESCOLHA UMA OPÇÃO: ")

        if opcao == '1':
            converter_real()
        elif opcao == '2':
            converter_dollar()
        elif opcao == '0':
            print("SAINDO.........")
            break 
        else:
            print("!!!!!! OPÇÃO INVALIDA. TENTE NOVAMENTE!!!!!")

menu()