from theta import Theta
import numpy as np

class NStepForecast:

    def __init__(self, process_input, process_output, theta: Theta, order: int) -> None:
        self._forecast = np.zeros(len(process_input))
        self._theta = theta
        self._order = order
        self._input = process_input
        self._output = process_output

    def append(self, index):
        if (self._is_inital_state(index)):
            self._forecast[index] = self._output[index]
            return
        self._forecast[index] = self._estimate(index)

    def get(self):
        return self._forecast

    def _is_inital_state(self, index):
        return index < self._order
    
    def _estimate(self, index):
        # yest_n[t] = -a1*yest_n[t-1] - a2*yest_n[t-2] + b1*dataframe['input'][t-1] + b2*dataframe['input'][t-2]
        forecast = 0
        for i, estimated_parameter in enumerate(self._theta.get()):
            if i < self._order:
                forecast -= estimated_parameter*self._forecast[index-i-1]
                continue
            forecast += estimated_parameter*self._input[index-i+self._order-1]

        return forecast
