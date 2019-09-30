 def CarregaAFD: 
    with open((sys.argv[1]), "r") as f:
        auxList1 = [line.strip().split(" ") for line in f]
