from gp import Population
from config import NUM_EVALUATIONS, IDEAL_RESULTS
from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler
from .convert import QiskitBuilder

class CircuitFitness:
    def __init__(self, population: Population):
        self.population = population
        
        self.qiskitcircuits = []
        self.fitnesses = []
        
    def makeqiskitcircuits(self):
        for circuit in self.population.members:
            qc = QiskitBuilder(circuit)
            self.qiskitcircuits.append(qc.build())
            
    def evaluatecircuit(self, qc: QuantumCircuit):
        qc.measure_all()
        sampler = StatevectorSampler()
        result = sampler.run([qc], shots=NUM_EVALUATIONS).result()
        
        result_dict = result[0].data.meas.get_counts()
        
        # evaluate circuit 
        total = 0
        length = len(IDEAL_RESULTS)
        
        for key in IDEAL_RESULTS:
            qb_ideal = IDEAL_RESULTS[key]
            
            try:
                qb_actual = result_dict[key]
            except KeyError:
                qb_actual = 0
            
            total += (qb_ideal - qb_actual)**2
        
        return total/length
        
            
    def makefitness(self):
        for qc in self.qiskitcircuits:
            self.fitnesses.append(self.evaluatecircuit(qc))
            
        # automatically add fitness to the population after this?
