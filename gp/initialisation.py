from config import POPULATION_SIZE, GATE_SET, NUM_WIRES, MAX_INITIAL_SIZE, MIN_INITIAL_SIZE
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
    # call create random gates and add to circuit
    num_gates = random.randint(MIN_INITIAL_SIZE, MAX_INITIAL_SIZE)
    c = Circuit([], NUM_WIRES) # initiliase circuit as empty
    
    for _ in range(num_gates):
        c.add_gate(create_random_gate())
        
    return c

    
    
def init_population() -> Population:
    # call create random circuits and add them to population
    p = Population([])
    for _ in range(POPULATION_SIZE):
        p.add_member(create_random_circuit())
        
    return p

