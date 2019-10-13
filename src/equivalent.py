def table_create(estados, alfabeto, transicoes, estados_finais):  # Cria a tabela de estados 
    equiv = []
    # tam = 7

    for n in estados[:(len(estados)-1)]: # Ex: 0, 1, 2, 3, 4 menos o ultimo
        for i in reversed(estados[1:]):  # Ex: 1, 2, 3, 4, 5 menos o primeiro

            equiv.append(equivalent_match(n,i,transicoes,alfabeto,estados_finais)) # n= estado1 , i= estado 2,
        # tam = tam-1
    
    equiv = list(filter(None, equiv))
    return equiv


def equivalent_match(sx,sy,transicoes,alfabeto,estados_finais): # retorna se equivalent (compara as transicoes )
    if sx == sy: #Se forem a mesma transicao já nem compara
        return None

    if not(is_estado_final(sx,estados_finais) == is_estado_final(sy, estados_finais)): #Se ambas não forem estados de aceitação ou o contrário, significa que não tem a mesma decisão para a palavra vazia, sendo não equivalentes
        return None

    for simbolo in alfabeto:#Verifica a equivalencia para cada letra do alfabeto, até achar a primeira a não ser equivalente
        linhaX = find_row(sx, simbolo, transicoes)# acha a linha com o estado, e o simbolo do alfabeto desta iteração
        linhaY = find_row(sy, simbolo, transicoes)

        if linhaX[2] != linhaY[2]:#se ambas forem para estados diferentes verifica se são estados finais/aceitação
            if not(is_estado_final(linhaX[2],estados_finais) and is_estado_final(linhaY[2], estados_finais)):#se ambas forem para estados diferentes de não aceitação devolvemos nada
                return None

    return [sx, sy]


def is_estado_final(estado, estados_finais):
    for estadoF in estados_finais:
        if estadoF == estado:
            return True
    return False

def find_row(estado, simbolo, transicoes):
    for linha in transicoes:
        if estado == linha[0] and simbolo == linha[1]:
            return linha
    return None

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