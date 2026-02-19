from gp import Population
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

            total+= fidelity_evaluation(expected, output_state)
            count += 1
        
        return total/count
      
    def makefitness(self, data: list[list[str], np.array]):
        # self.inputqubits = inputqubits
        for qc in self.qiskitcircuits:
            self.fitnesses.append(self.evaluatecircuit(qc, data))
            
            
        # automatically add fitness to the population after this?
        
def fidelity_evaluation(expected, output_state):

    fidelity = abs(np.vdot(expected, output_state.data)) ** 2

    #total += (1-fidelity) # for minimising fitness
    
    return fidelity # sqrt just to change briefly
    
def test_evaluation(expected, output_state):
    candidate = output_state.data
    target = expected

    # -------------------------
    # 1️⃣ Amplitude fitness
    # -------------------------
    amp_error = np.linalg.norm(np.abs(target) - np.abs(candidate))
    F_amp = 1 / (1 + amp_error)

    # -------------------------
    # 2️⃣ Relative phase fitness
    # -------------------------
    # Choose reference index with non-zero amplitude
    ref = np.argmax(np.abs(target))

    phase_diff = np.angle(candidate * np.conj(target))

    # Normalize relative to reference phase
    rel_phase_error = np.linalg.norm(phase_diff - phase_diff[ref])
    F_phase = 1 / (1 + rel_phase_error)

    # -------------------------
    # 3️⃣ Fidelity (your original)
    # -------------------------
    fidelity = abs(np.vdot(target, candidate)) ** 2
    F_fid = fidelity

    # -------------------------
    # Combine (weights adjustable)
    # -------------------------
    w_amp = 0.4
    w_phase = 0.3
    w_fid = 0.3

    return (w_amp * F_amp + w_phase * F_phase + w_fid * F_fid)