class Gate:
    def __init__(self, name: str, arity: int = 0, param_num: int = 0):
        self.name = name
        self.arity = arity
        self.param_num = param_num
        
    @property
    def wires(self) -> list[int]:
        return self._wires
        
    @wires.setter
    def wires(self, wires: list[int]):
        if len(wires) == self.arity:
            raise ValueError(f"{self.arity} wires expected, {len(wires)} given.")
        
        self._wires = wires
      
    @property  
    def param(self) -> list[int]:
        return self._param
    
    @param.setter
    def param(self, param: list[int]):
        if len(param) != self.param_num:
            raise ValueError(f"{self.param_num} parameters expected, {len(param)} given")
            
        self.param = param
        

    
    
        
        
        
        
# NOTE
# hadamard - only one wire possible (pure hadamard)
# cnot - must have twoc
# this idea needs to be enforced when altering the wires 

# ensure the length of the wire array is maintained 
# include class functions like "change wire" or "change param"    

# mutation can happen within the wires - want this to be seperate from any GP work - no random, just take inputs and give outputs 
# mutation can happen with angle parameters 


# we dont want a seperate gate definition for each possible pair of wires - whats a neat way of 