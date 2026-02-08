#from gp import initialisation, operations
from config import check_prob, CUMULATIVE_PROB, build_cumulative_prob
from gp import initialisation

"""
c1 = initialisation.create_random_circuit()
c2 = initialisation.create_random_circuit()

print(f"Parent 1: {c1}")
print(f"Parent 2: {c2}")

# cutoff point between 1 and 3
print(f"Left: {c1.circuit[:2:]}")
print(f"Middle: {c1.circuit[2:3:]}")
print(f"Right: {c1.circuit[3::]}")

children = operations.insertion(c1, c2)

print("child 1: ", children[0])
print("child two: ", children[1])
"""

print(check_prob)

c = initialisation.create_random_circuit(5, 5)
print(c)

print(CUMULATIVE_PROB)
build_cumulative_prob()
print(CUMULATIVE_PROB)
