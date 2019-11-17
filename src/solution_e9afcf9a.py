from utils import *
import numpy as np


filename = 'e9afcf9a.json'


def process_data(*args):
    output = []
    for training_data in data['train']:
        array = to_numpy_array(training_data['input'])
        output_grid = to_output_array(array)
        n_rows, n_cols = np.shape(output_grid)
        for i in range(n_rows-1):
            for j in range(n_cols):
                output_grid[i, j] = array[i+1, j]
        output.append(output_grid.tolist())
    return output, data['test']


# This is main handler for the proram
if __name__ == "__main__":
    data = load_json(filename)
    output_grid, test = process_data(data)
    print(output_grid, test)
