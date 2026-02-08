# representation [[gate, wires, params], ...]

from config import NUM_GENERATIONS, CUMULATIVE_PROB, build_cumulative_prob
from .initialisation import init_population
from evaluation import CircuitFitness
from .operations import *
from .population import Population
from .data_process import get_data
import random
import numpy as np

def evolution() -> Population:
    
    # initialisation 
    population = init_population()
    
    print(population)
    
    #process data here - create two arrays- input and expected_out
    
    data = get_data()
    build_cumulative_prob()

    for _ in range(NUM_GENERATIONS):
        #evaluate 
        cf = CircuitFitness(population)
        cf.makeqiskitcircuits()
        cf.makefitness(data)
        population.fitnesses = cf.fitnesses
        
        # print(population.fitnesses)
        
        next_population = Population([])
        
        while next_population.size < population.size:
            r = random.random()
            
            if r < CUMULATIVE_PROB['crossover'] and next_population.size + 2 <= population.size:
                parent_one = selection(population)
                parent_two = selection(population)
                
                children = crossover(parent_one, parent_two)
                next_population.add_member(children[0])
                next_population.add_member(children[1])
                
            elif r < CUMULATIVE_PROB['insertion'] and next_population.size + 2 <= population.size:
                parent_one = selection(population)
                parent_two = selection(population)
                
                children = insertion(parent_one, parent_two)
                next_population.add_member(children[0])
                next_population.add_member(children[1])
                
            elif r < CUMULATIVE_PROB['mutation']:
                parent = selection(population)
                child = mutation(parent)
                
                next_population.add_member(child)
                
            elif r < CUMULATIVE_PROB['insert_mutation']:
                parent = selection(population)
                child = insert_mutation(parent)
                
                next_population.add_member(child)
                
            else: # shrink mutation
                parent = selection(population)
                child = shrink_mutation(parent)
                
                next_population.add_member(child)
        
        population.overwrite_from(next_population)
        
    cf = CircuitFitness(population)
    cf.makeqiskitcircuits()
    
    # make fitness should take in the processed data - dont need to loop over
    # then the 
    
    cf.makefitness(data)
    population.fitnesses = cf.fitnesses
    
    print("\n------------------------------------------------------------\n")
    print("BEST FITNESSES: ", max(population.fitnesses))
    print("\n------------------------------------------------------------\n")
    
    print("\n------------------------------------------------------------\n")
    print("AVERAGE FITNESSES: ", np.mean(population.fitnesses))
    print("\n------------------------------------------------------------\n")
        
    return population


    
    