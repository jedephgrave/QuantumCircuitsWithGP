from gp import initialisation
from evaluation import CircuitFitness
from gp import operations

from circuit import Circuit, Gate

from gp import gp, Population

def main():
    p = gp.evolution()
    print(p)
    

if __name__ == "__main__":
    main()