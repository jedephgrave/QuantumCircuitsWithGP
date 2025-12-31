from circuit import Circuit, Gate
from config import POPULATION_SIZE
import random


class Population:

    def __init__(self, members: list[Circuit]):
        self.members = members
        self.size = len(members)
        self.fitnesses = []
        
    def add_member(self, circuit: Circuit):
        if self.size == POPULATION_SIZE:
            return ValueError(f"Population at limit of {POPULATION_SIZE}.")
        
        self.members.append(circuit)
        self.size += 1
        
    @property
    def fitnesses(self) -> list[int]:
        return self._fitnesses
    
    @fitnesses.setter
    def fitnesses(self, fitnesses: list[int]):
        if len(fitnesses) != self.size:
            raise ValueError(f"List of size {self.size} expected, size of {len(fitnesses)} given.")
        
        self._fitnesses = fitnesses
        
    def member(self, index: int):
        if index >= self.size:
            return ValueError(f"Index between 0 and {self.size-1} expected, index of value {index} given.") 
        
        return self.members[index]
    
    # return one random member of the population
    def rand_member(self):
        r = random.randint(0, self.size-1)
        
        return self.members[r]

    # return a given number of random members from the population
    def rand_members(self, number):
        if number > self.size or self.size <= 0:
            return ValueError(f"Number between 1 and {self.size} expected, number less than or greater than population size given.")
        
        return random.sample(self.members, number)
        
    # return formatted string of circuit strings and their respective fitnesses    
    def __str__(self) -> str:
        population_array = []
        for circuit in self.members:
            population_array.append(str(circuit))
        
        return f"{population_array}"