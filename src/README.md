# Hand Coded Solution for the Abstraction and Reasoning Corpus (ARC)

This part of the repository contains the implementation of *Abstraction and Reasoning Corpus* solution using `python`. This was created as per requirement for `Assignment 3` for *Programming and Tools in Artificial Intelligence* Module. Here we provide the code that provides the solution for the three input files given as 3 tasks in the ARC. 

The 3 tasks that are solved in this are:

* 25ff71a9.json
* e9afcf9a.json
* f76d97a5.json

## Solution Approach

The solution approach includes the identification of shape of the grid, colour patterns inside the input grid and how the colour patterns and shapes are coded as output grid. 

Following libraries are used to code the solution and get the desired output.

* json
* numpy

Each solution involves the json file to be provided as input for the execution and desired output is achieved. Following is the example execution to get the desired output.

```bash
$ python3 solution_25ff71a9.py ./25ff71a9.json 
{"output": [[0, 0, 0], [1, 1, 1], [0, 0, 0]]}

{"output": [[0, 0, 0], [0, 0, 0], [1, 1, 1]]}

{"output": [[0, 0, 0], [0, 1, 0], [1, 1, 0]]}

{"output": [[0, 0, 0], [0, 2, 2], [0, 0, 2]]}

{"output": [[0, 0, 0], [2, 0, 0], [2, 0, 0]]}

{"output": [[0, 0, 0], [0, 0, 0], [0, 1, 0]]}
```

## Code Execution

The main handler takes the input file as system argument and then passes the filename to the `ProcessData` class which initializes the variables and execute some basic functions for the solution to be processed further in file `utils.py`. 

- Read the json object from the file.
- Get the train grid from the json object.
- Get the test grid from the json object.

These functions are private to the class and are called as soon as class is created. This same approach is used across all the solutions since we want to avoid repeatable approach and use as much code as possible in common ways. 

```bash
class ProcessData():

    # init method or constructor
    def __init__(self, filename):
        """
        These are set of initial variables that are 
        created when this class is initialized.
        """
        self.filename = filename
        self.data = None
        self.input_grid = []
        self.eval_grid = []
        self._load_json()
        self._get_train_grid_from_json()
        self._get_eval_grid_from_json()

    def _load_json(self):
        """
        This function takes the filename as input and 
        laods the json in to the object for further
        processing.
        """
        with open(self.filename) as json_file:
            self.data = json.load(json_file)

    def _get_train_grid_from_json(self):
        """
        This function reads the input data from the train
        block and also reads the output data so that we 
        can test against our generated output.
        """
        for d in self.data['train']:
            self.input_grid.append(np.array(d['input']))

    def _get_eval_grid_from_json(self):
        for d in self.data['test']:
            self.eval_grid.append(np.array(d['input']))
```

### Solution 1

The solution to `25ff71a9.json` involves shifting the numpy array on axis=1. This approach makes use of the internal numpy library `np.roll` which makes it lot easier to get the desired output.

```bash
def roll_np_array(arr, shift, axis=0):
    """
    This function rolls the numpy array based
    on shift value and axis provided.
    """
    return np.roll(arr, shift, axis=axis)
```

### Solution 2

The solution to `e9afcf9a.json` involves copying the input grid to output grid for processing. There after we iterate through all the columns and at every even steps we move the cells around to swap the digits in the rows for that column. 

The final grid is the desired output that is produced.

```bash
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
```

### Solution 3

The solution to `f76d97a5.json` involves copying the input grid to output grid for processing. There after we flip the array based on the color patters that the original array holds and then change all 5's to 0's for getting the final output that is desired.

```bash
def solve(input_grid):
    """
    Here we have solve function that takes the input grid
    and produces the output grid based on the below logic.
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
```
