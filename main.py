from gp import initialisation
from evaluation import CircuitFitness

p = initialisation.init_population()

print(p)

cf = CircuitFitness(p)

cf.makeqiskitcircuits()
cf.makefitness()


p.fitnesses = cf.fitnesses

print(p)

print("\n\n\nYOO\n\n\n")

print(p.sample_population(4))