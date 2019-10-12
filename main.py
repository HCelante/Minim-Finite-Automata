import sys
import src.equivalent as eq # reponsavel por buscar os estados equivalentes
 

def main():
    with open((sys.argv[1]), "r") as f: # recebe o arquivo por parametro
        auxList1 = [line.strip().split(" ") for line in f] # armazena em uma lista
    if auxList1 == None:
        print("\nNao foi possivel carregar o LFA!\nExecute o codigo novamente passando o txt correto por parametro.\n")
    else:
        print("Procurando estados equivalentes...")
        alfabeto = auxList1[0]
        Equivalent = eq.table_create(auxList1[3], alfabeto)
        if Equivalent == None:
            print("Nao foram encontrados estados equivalentes!")
        else:
            print("Estados equivalentes encontrados:")
            print(Equivalent)


if __name__ == "__main__":
    main()