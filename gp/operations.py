# crossover (selection too) and mutation functions needed
from .population import Population
from circuit import Circuit
from config import TOURNAMENT_SIZE
import random, math

def selection(population: Population):
    # select based on tournmanet size
    
    sample = population.sample_population(TOURNAMENT_SIZE)
    
    best_fitness = math.inf
    best_circuit = None
    
    for index in TOURNAMENT_SIZE:
        member_fitness = sample.fitnesses[index]
        member_circuit = sample.member(index)
        
        if member_fitness < best_fitness:
            best_fitness = member_fitness
            best_circuit = member_circuit
            
    return best_circuit
 
    