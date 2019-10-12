def table_create(lista, alfabeto, transicoes):  # Cria a tabela de estados 
    equiv = []
    
    for n in lista[:(len(lista)-1)]: # Ex: 0, 1, 2, 3, 4 menos o ultimo
        for i in lista.reverse[1:]:  # Ex: 1, 2, 3, 4, 5 menos o primeiro
            for a in alfabeto:       # testa para cada letra
                equiv.append(equivalent_match(n,i,a,transicoes)) # n= estado1 , i= estado 2, a= letra
    return equiv


def equivalent_match(sx,sy,signal,transicoes): # retorna se equivalent
    pass