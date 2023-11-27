import numpy as np

np.random.seed(0)

def activation(array = ...):
    return np.heaviside(array, 0)

#print(step_function(np.random.uniform(-1, 1, (10, 2))))