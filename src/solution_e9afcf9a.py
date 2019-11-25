from utils import ProcessData, to_output_array, \
    get_shape_of_array, output_to_json


def solve(input_grid):
    """
    Here we have solve function that takes the input grid
    and produces the output grid based on the below logic.
    """
    _output_grid = to_output_array(input_grid)
    _, n_cols = get_shape_of_array(input_grid)
    for i in range(n_cols):
        if (i % 2):
            _output_grid[0, i] = input_grid[1, i]
            _output_grid[1, i] = input_grid[0, i]
    return output_to_json(_output_grid)


# This is main handler for the proram
if __name__ == "__main__":
    pd = ProcessData(__file__)
    for idx in range(len(pd.input_grid)):
        output = solve(pd.input_grid[idx])
        print(output + '\n')
    for idx in range(len(pd.eval_grid)):
        output = solve(pd.eval_grid[idx])
        print(output)
