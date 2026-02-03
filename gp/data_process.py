import pandas as pd
import numpy as np
import ast

from pathlib import Path


# function?
# returns both qubit input and expected output arrays

def get_data() -> list[list[str], np.array]:
    
    # data file location
    current = Path(__file__).resolve()
    root = current.parent.parent
    path = root / 'test_data.csv'
    
    
    df = pd.read_csv(path)
    
    x = df['qubit_input'].tolist()
    
    # parse from string to useable numpy array
    
    y = []
    for value in df['expected_output']:
        parsed = ast.literal_eval(value)
        np_arr = np.array(parsed, dtype=np.complex128)
        y.append(np_arr)
    
    #y = np.array(df['expected_output'].tolist())
    
    return [x,y]