import numpy as np

class MSE:
    
    def __init__(self, process_output, process_forecast) -> None:
        self._mse = np.sum((process_output-process_forecast)**2) / (len(process_output)-2)

    def get(self):
        return self._mse