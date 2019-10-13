def table_create(estados, alfabeto, transicoes):  # Cria a tabela de estados 
    equiv = []
    
    for n in estados[:(len(estados)-1)]: # Ex: 0, 1, 2, 3, 4 menos o ultimo
        for i in reversed(estados[1:]):  # Ex: 1, 2, 3, 4, 5 menos o primeiro

            equiv.append(equivalent_match(n,i,transicoes)) # n= estado1 , i= estado 2,
    return equiv


def equivalent_match(sx,sy,transicoes): # retorna se equivalent (compara as transicoes )
    pass

def unreachable_states(estados, estados_iniciais, transicoes):
    mantidos = []
    aindaha = True

    while aindaha:
        tamanhoant = len(mantidos)
        mantidos = []
        mantidos = mantidos + estados_iniciais
        # for estd in transicoes:
            #print(estd[0])
        for tr in transicoes:
                #print(tr)
            if(tr[2] != tr[0]):
                mantidos.append(tr[2])
        mantidos = set(mantidos)
        if len(mantidos) == tamanhoant:
            aindaha = False 
    mantidos = list(sorted(mantidos))
    print("Estados:    ", estados)
    print("Pós função: ", mantidos)
    return mantidos