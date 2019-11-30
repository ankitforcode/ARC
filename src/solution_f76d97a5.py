import sys
from utils import ProcessData, to_output_array, \
    get_shape_of_array, get_unique_items, output_to_json


def solve(input_grid):
    """
    Here we have solve function that takes the input grid. 
    we flip the array based on the color patterns that the 
    original array holds and then change all 5's to 0's 
    for getting the final output that is desired
    """
    _output_grid = to_output_array(input_grid)
    n_rows, n_cols = get_shape_of_array(input_grid)
    unique_items = get_unique_items(input_grid)
    for i in range(n_rows):
        for j in range(n_cols):
            if input_grid[i, j] == unique_items[0]:
                _output_grid[i, j] = unique_items[1]
            else:
                _output_grid[i, j] = unique_items[0]
            _output_grid[_output_grid == 5] = 0
    return output_to_json(_output_grid)


# This is main handler for the proram
if __name__ == "__main__":
    pd = ProcessData(sys.argv[1])
    for idx in range(len(pd.input_grid)):
        output = solve(pd.input_grid[idx])
        print(output + '\n')
    for idx in range(len(pd.eval_grid)):
        output = solve(pd.eval_grid[idx])
        print(output + '\n')
