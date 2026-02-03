# crossover (selection too) and mutation functions needed
from .population import Population
from circuit import Circuit
from config import TOURNAMENT_SIZE, GATE_SET
import random, math

def selection(population: Population):
    # select based on tournmanet size
    
    sample = population.sample_population(TOURNAMENT_SIZE)
    
    best_fitness = 0
    best_circuit = None
    
    for index in range(TOURNAMENT_SIZE):
        member_fitness = sample.fitnesses[index]
        member_circuit = sample.member(index)
        
        if member_fitness > best_fitness:
            best_fitness = member_fitness
            best_circuit = member_circuit
            
    return best_circuit

# for minimising fitness function - depends on it
# LEGACY
def selection_min(population: Population):
    # select based on tournmanet size
    
    sample = population.sample_population(TOURNAMENT_SIZE)
    
    best_fitness = math.inf
    best_circuit = None
    
    for index in range(TOURNAMENT_SIZE):
        member_fitness = sample.fitnesses[index]
        member_circuit = sample.member(index)
        
        if member_fitness < best_fitness:
            best_fitness = member_fitness
            best_circuit = member_circuit
            
    return best_circuit
 
def crossover(parent_one: Circuit, parent_two: Circuit) -> list[Circuit]:
    #pick two random points (one on each circuit)
    # split at random point - 1 -> 1.1 and 1.2, 2 -> 2.1 and 2.2
    # Circuit 1.1 merge with circuit 2.2, Circuit 1.2 merge with circuit 2.1
    # return them (new children) in an array
    
    split_one = random.randint(0, parent_one.length - 2)
    split_two = random.randint(0, parent_two.length - 2)
    
    parent_one_a, parent_one_b = parent_one.split(split_one)
    parent_two_a, parent_two_b = parent_two.split(split_two)
    
    children = [parent_one_a.combine(parent_two_b), parent_two_a.combine(parent_one_b)]
    
    return children

def mutation(parent: Circuit) -> Circuit:
    # mutate one gate in the circuit to another random one 
    
    new_gate = random.choice(GATE_SET)
    position = random.randint(0, parent.length - 1)
    
    parent.swap(position, new_gate)
    
    return parent


# a generalised crossover - can be any given middle section from the circuit (cut at two points)
def insertion(parent_one: Circuit, parent_two: Circuit) -> list[Circuit]:
    pass