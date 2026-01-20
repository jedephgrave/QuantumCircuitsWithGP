# representation [[gate, wires, params], ...]

from config import NUM_GENERATIONS
from .initialisation import init_population
from evaluation import CircuitFitness
from .operations import selection, crossover, mutation
from .population import Population
import random

def evolution() -> Population:
    
    # initialisation 
    population = init_population()

    for _ in range(NUM_GENERATIONS):
        #evaluate 
        cf = CircuitFitness(population)
        cf.makeqiskitcircuits()
        cf.makefitness()
        population.fitnesses = cf.fitnesses
        
        print(population.fitnesses)
        
        next_population = Population([])
        
        while next_population.size < population.size:
            r = random.random()
            
            if r < 0.8 and not(next_population.size + 2 > population.size):
                parent_one = selection(population)
                parent_two = selection(population)
                
                children = crossover(parent_one, parent_two)
                next_population.add_member(children[0])
                next_population.add_member(children[1])
            else:
                parent = selection(population)
                child = mutation(parent)
                
                next_population.add_member(child)
        
        population.overwrite_from(next_population)
        
    cf = CircuitFitness(population)
    cf.makeqiskitcircuits()
    cf.makefitness()
    population.fitnesses = cf.fitnesses
    
    print("FINAL FITNESSES: ", population.fitnesses)
        
    return population


    
    