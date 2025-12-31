from .gate import Gate

class Circuit:
    
    def __init__(self, circuit: list[Gate], num_wires: int):
        self.circuit = circuit
        self.length = len(circuit)
        self.num_wires = num_wires
        
    def add_gate(self, gate: Gate):
        self.circuit.append(gate)
        self.length += 1
        
    def split(self, cutoff: int):
        if not(0 <= cutoff < self.length-1 ):
            raise ValueError(f"Cutoff between 0 and {self.length - 1} expected ,value of {cutoff} given.")
        
        # split circuit into two seperate circuit objects 
        left = self.circuit[:cutoff+1:]
        right = self.circuit[cutoff+1::]
        
        return Circuit(left), Circuit(right)
        
    def combine(self, circuit: "Circuit"):
        left = self.circuit
        right = circuit.circuit
        
        combination = left + right
        
        return Circuit(combination)

    def __str__(self) -> str:
        circuit_array = []
        for gate in self.circuit:
            circuit_array.append(str(gate))
        
        return f"{circuit_array}"


    
        
    