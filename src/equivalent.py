def table_create(lista, alfabeto):
    equiv = []
    for a in alfabeto:
        for n in lista[:(len(lista)-1)]:
            for i in lista.reverse[1:]:
            
                equiv.append(equivalent_match(n,i,a))


    if True:
        return equiv
    else:
        return None


def equivalent_match(sx,sy,signal): # retorna se equivalent
    pass