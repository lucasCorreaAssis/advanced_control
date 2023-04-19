import numpy as np

class Fi:
    def __init__(self, process_input, process_output, order: int) -> None:
        self._order = order
        self._input = process_input
        self._output = process_output
        self._fi = np.empty((0, order * 2))

    def append(self, index):
        if (self._is_inital_state(index)):
            self._fi = np.vstack((self._fi, self._get_initial_state()))
            return
        self._fi = np.vstack((self._fi, self._estimate(index)))

    def get(self):
        return self._fi
    
    def _is_inital_state(self, index):
        return index <= self._order-1
    
    def _get_initial_state(self):
        return [-self._output[0] if i < self._order else 0 for i in range(self._order*2)]

    def _estimate(self, index):
        output_estimate = [-self._output[index - i * 1] for i in range(1, self._order+1)]
        input_estimate = [self._input[index - i * 1] for i in range(1, self._order+1)]
        return np.concatenate((output_estimate, input_estimate))
