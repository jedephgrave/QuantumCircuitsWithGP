class Gate:
    def __init__(self, name: str, arity: int = 0, param_num: int = 0):
        self.name = name
        self.arity = arity
        self.param_num = param_num
        
        self._wires = None
        self._param = None
        
    @property
    def wires(self) -> list[int]:
        return self._wires
        
    @wires.setter
    def wires(self, wires: list[int]):
        if len(wires) != self.arity:
            raise ValueError(f"{self.arity} wires expected, {len(wires)} given.")
        
        self._wires = wires
      
    @property  
    def param(self) -> list[int]:
        return self._param
    
    @param.setter
    def param(self, param: list[int]):
        if len(param) != self.param_num:
            raise ValueError(f"{self.param_num} parameters expected, {len(param)} given")
            
        self._param = param
        
    def __str__(self) -> str:
        return f"({self.name}, {self.wires}, {self.param})"
        