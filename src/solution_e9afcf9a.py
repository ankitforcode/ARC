from utils import *
import numpy as np


filename = 'e9afcf9a.json'


def process_data(*args):
    output_data = []
    for training_data in data['train']:
        input_grid = to_numpy_array(training_data['input'])
        test_grid = to_numpy_array(training_data['output'])
        output_grid = to_output_array(input_grid)
        _, n_cols = np.shape(output_grid)
        for i in range(n_cols):
            if (i % 2):
                output_grid[0, i] = input_grid[1, i]
                output_grid[1, i] = input_grid[0, i]
        if np.array_equal(output_grid, test_grid):
            output_data.append(output_grid.tolist())
    return output_data


# This is main handler for the proram
if __name__ == "__main__":
    data = load_json(filename)
    output_grid = process_data(data)
