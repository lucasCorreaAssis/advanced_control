import numpy as np
from fi import Fi

class Theta:
    def __init__(self, fi: Fi, process_output) -> None:
        self._theta = np.linalg.inv(fi.get().T @ fi.get()) @ fi.get().T @ process_output

    def get(self):
        return self._theta
    
    def set(self, index, value):
        self._theta[index] = value
