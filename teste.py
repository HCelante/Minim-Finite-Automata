import sys

def CarregaAFD(): 
  with open((sys.argv[1]), "r") as ponteiro:
    automato = [line.strip().split(" ") for line in ponteiro]
    return automato

def main():
  # automato = []
  automato = CarregaAFD()
  for line in automato:
      print(line)

  
if __name__ == "__main__":
  main()