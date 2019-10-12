def table_create(lista, alfabeto):  # Cria a tabela de estados 
    equiv = []
    
    for n in lista[:(len(lista)-1)]: # Ex: 0, 1, 2, 3, 4 menos o ultimo
        for i in lista.reverse[1:]:  # Ex: 1, 2, 3, 4, 5 menos o primeiro
            for a in alfabeto:       # testa para cada letra
                equiv.append(equivalent_match(n,i,a)) # n= estado1 , i= estado 2, a= letra


    if True:
        return equiv
    else:
        return None


def equivalent_match(sx,sy,signal): # retorna se equivalent
    pass