import sys
from utils import ProcessData, to_output_array, \
    roll_np_array, output_to_json


def solve(input_grid):
    """
    Here we have solve function that takes the input grid,
    Use numpy.roll function created in utils.py to
    rolls the numpy array based on shift value and axis=1 provided
    to give the desired output.
    """
    _output_grid = roll_np_array(input_grid, 1)
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
