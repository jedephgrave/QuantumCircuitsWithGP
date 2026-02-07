from circuit import Gate 

GATE_SET = [
    Gate('H', 1, 0),   
    Gate('SWAP', 2, 0),
    Gate('SN', 2, 0),
]

# dont use this - just to list extra gates not currently being used
SPARE_GATE_SET = [
    Gate('X', 1, 0),
    Gate('CN', 2, 0),
    Gate('S', 1, 0),
]

NUM_WIRES = 2

# gp hyperparameters go here 
POPULATION_SIZE = 100

INITIAL_SIZE = {'max': 4,
                'min': 3
                }

# maybe add a max insertion size for the chunks?

MUTANT_INSERT_SIZE = {'max': 3,
                      'min': 2
                      }
MUTANT_SHRINK_SIZE = {'max': 2,
                      'min': 1
                      }

PROB_DICT = {'crossover' : 0.35,
             'insertion': 0.3,
             'mutation': 0.15,
             'insert_mutation': 0.1,
             'shrink_mutation': 0.1
             }

# ensure to run this before gp begins run
check_prob = sum(PROB_DICT.values()) == 1
    
           

# evaluation variables go here (ideal circuit outputs, times evaluated)

NUM_EVALUATIONS = 100

IDEAL_RESULTS = {
    '00': NUM_EVALUATIONS/2,
    '01': 0,
    '10': 0,
    '11': NUM_EVALUATIONS/2
}

# gp variables

NUM_GENERATIONS = 40

TOURNAMENT_SIZE = 5



