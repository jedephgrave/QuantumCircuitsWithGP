from circuit import Gate 

GATE_SET = [
    Gate('H', 1, 0),
    Gate('CN', 2, 0),
]

# dont use this - just to list extra gates not currently being used
SPARE_GATE_SET = [
    Gate('X', 1, 0),
]

NUM_WIRES = 2

# gp hyperparameters go here 
POPULATION_SIZE = 20
INITIAL_SOLUTION_SIZE = 3

# evaluation variables go here (ideal circuit outputs, times evaluated)

NUM_EVALUATIONS = 100

IDEAL_RESULTS = {
    '00': NUM_EVALUATIONS/2,
    '01': 0,
    '10': 0,
    '11': NUM_EVALUATIONS/2
}

# gp variables

NUM_GENERATIONS = 10

TOURNAMENT_SIZE = 2 



