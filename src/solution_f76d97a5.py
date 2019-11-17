from utils import *
import numpy as np


filename = 'f76d97a5.json'


def process_data(*args):
    output_data = []
    for training_data in data['train']:
        array = to_numpy_array(training_data['input'])
        test_grid = to_numpy_array(training_data['output'])
        output_grid = to_output_array(array)
        n_rows, n_cols = np.shape(output_grid)
        unique_items = np.unique(output_grid)
        for i in range(n_rows):
            for j in range(n_cols):
                if output_grid[i, j] == unique_items[0]:
                    output_grid[i, j] = unique_items[1]
                else:
                    output_grid[i, j] = unique_items[0]
        output_grid = np.where(output_grid == 5, 0, output_grid)
        if np.array_equal(output_grid, test_grid):
            output_data.append(output_grid.tolist())
    return output_data


# This is main handler for the proram
if __name__ == "__main__":
    data = load_json(filename)
    output_grid = process_data(data)
    print(output_grid)
