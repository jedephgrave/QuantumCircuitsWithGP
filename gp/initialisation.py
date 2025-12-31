from config import POPULATION_SIZE, INITIAL_SOLUTION_SIZE, GATE_SET, NUM_WIRES
from circuit import Circuit, Gate
from .population import Population
import random


# init the population 
    # create random genomes less than or equal to size
    
# TODO - add parameters to gate creation
def create_random_gate():
    wire_values = list(range(0, NUM_WIRES))
    
    gate = random.choice(GATE_SET)
    
    # random sample from wire_values based on arity
    
    gate.wires = random.sample(wire_values, gate.arity)
    
    return gate
    
def create_random_circuit() -> Circuit:
    # pick a random number of gates (1 to initial solution size)
    # loop the random number of times - randomly select gate from gate set - add to array
    # after built - create circuit object and return
    num_gates = random.randint(1, INITIAL_SOLUTION_SIZE)
    print(num_gates)
    c = Circuit([], NUM_WIRES) # initiliase circuit as empty
    
    for _ in range(num_gates):
        c.add_gate(create_random_gate())
        
    return c

    
    
def init_population() -> Population:
    # create random circuits
    # create circuits until population size 
    # add each to array - then create population object 
    p = Population([])
    for _ in range(POPULATION_SIZE):
        p.add_member(create_random_circuit())
        
    return p

