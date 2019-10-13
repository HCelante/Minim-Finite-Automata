import sys
import src.equivalent as eq # reponsavel por buscar os estados equivalentes
 

def main():
    with open((sys.argv[1]), "r") as f: # recebe o arquivo por parametro
        auxList1 = [line.strip().split(" ") for line in f] # armazena em uma lista
    if auxList1 == None:
        print("\nNao foi possivel carregar o LFA!\nExecute o codigo novamente passando o txt correto por parametro.\n")
    else:
        print("Procurando estados equivalentes...")
        alfabeto = auxList1[1]
        estados = auxList1[3]
        estados_finais = auxList1[5]
        estados_iniciais = auxList1[4]
        branco = auxList1[2]
        transicoes = auxList1[6:]
        estados = eq.unreachable_states(estados, estados_iniciais, transicoes)
        Equivalent = eq.table_create(estados, alfabeto, transicoes, estados_finais)
        if Equivalent == None:
            print("Nao foram encontrados estados equivalentes!")
        else:
            print("Estados equivalentes encontrados:")
            for linha in Equivalent:
                print(linha)


if __name__ == "__main__":
    main()