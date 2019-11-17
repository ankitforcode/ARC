from utils import *
import numpy as np


filename = '25ff71a9.json'


def process_data(*args):
    output_data = []
    for training_data in data['train']:
        input_grid = to_numpy_array(training_data['input'])
        test_grid = to_numpy_array(training_data['output'])
        output_grid = to_output_array(input_grid)
        n_rows, _ = np.shape(output_grid)
        output_grid[0, :] = input_grid[n_rows-1, :]
        for i in range(n_rows-1):
            output_grid[i+1, :] = input_grid[i, :]
        if np.array_equal(output_grid, test_grid):
            output_data.append(output_grid.tolist())
    return output_data


# This is main handler for the proram
if __name__ == "__main__":
    data = load_json(filename)
    output_grid = process_data(data)
    print(output_grid)
