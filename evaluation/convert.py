from qiskit import QuantumCircuit
from circuit import Circuit, Gate


class QiskitBuilder:
    def __init__(self, circuit: Circuit):
        self.circuit = circuit
        self.qc = QuantumCircuit(self.circuit.num_wires) # create qiskit object with matching qubit num
        
        self.gates = {
            "H": self.hadamard,
            "CN": self.cnot,
            
        }
        
    # class methods:
        # builder methods
        # methods for each 
        
    # add error for unknown gate?
        
    def build(self):
        for gate in self.circuit.circuit:
            self.gates[gate.name](gate.wires)
        return self.qc
        
    def hadamard(self, wires: list[int]):
        self.qc.h(wires[0])
    
    def cnot(self, wires: list[int]):
        self.qc.cx(wires[0], wires[1])


# call fitness on whole population - 
# take in a given circuit
# convert the circuit 
# return the qiskit circuit
# evaluate the qiskit circuit and return this evaluation