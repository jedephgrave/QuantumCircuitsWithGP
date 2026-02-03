from gp import Population
from config import NUM_EVALUATIONS, IDEAL_RESULTS
from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler
from qiskit.quantum_info import Statevector
from .convert import QiskitBuilder
import numpy as np

class CircuitFitness:
    def __init__(self, population: Population):
        self.population = population
        
        self.qiskitcircuits = []
        self.fitnesses = []
        self.inputqubits = ['00']
        
    def makeqiskitcircuits(self):
        for circuit in self.population.members:
            qc = QiskitBuilder(circuit)
            self.qiskitcircuits.append(qc.build())
            
    def evaluatecircuit(self, qc: QuantumCircuit, data: list[list[str], np.array]) -> int:

        total = 0
        count = 0
        
        data = zip(data[0], data[1])
        
        for in_qubits, expected in data:

            input_state = Statevector.from_label(in_qubits)
            output_state = input_state.evolve(qc)
            
            fidelity = abs(np.vdot(expected, output_state.data)) ** 2
            total += fidelity # for maximising fitness
            #total += (1-fidelity) # for minimising fitness
            count += 1
            
        
        return total/count
        
            
    def makefitness(self, data: list[list[str], np.array]):
        # self.inputqubits = inputqubits
        for qc in self.qiskitcircuits:
            self.fitnesses.append(self.evaluatecircuit(qc, data))
            
            
        # automatically add fitness to the population after this?
