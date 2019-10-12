import sys
import src.equivalent as eq
 

def main():
    with open((sys.argv[1]), "r") as f:
        auxList1 = [line.strip().split(" ") for line in f]
    if auxList1 == None:
        print("\nNao foi possivel carregar o LFA!\nExecute o codigo novamente passando o txt correto por parametro.\n")
    else:
        print("Procurando estados equivalentes...")
        alfabeto = auxList1[0]
        Equivalent = eq.table_create(auxList1[7:], alfabeto)
        if Equivalent == None:
            print("Nao foram encontrados estados equivalentes!")
        else:
            print("Estados equivalentes encontrados:")
            print(Equivalent)


if __name__ == "__main__":
    main()