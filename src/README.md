# Hand Coded Solution for the Abstraction and Reasoning Corpus (ARC)

This part of the repository contains the implementation of Abstraction and Reasoning Corpus solution using python. This was created as per requirement for Assignment 3 for Programming and Tools in Artificial Intelligence Module. Here we provide the code that provides the solution for the three input files given as 3 tasks in the ARC. 

The 3 tasks that are solved in this are:

* 25ff71a9.json
* e9afcf9a.json
* sf76d97a5.json

## Solution Approach

The solution approach includes the identification of shape of the grid, colour patterns inside the input grid and how the colour patterns and shapes are coded as output grid. 

Following libraries are used to code the solution and get the desired output.

* json
* numpy

Each solution involves the json file to be provided as input for the execution and desired output is acheived. Following is the example execution to get the desired output.

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

1. The first approach to the solution involves shifting the numpy array on axis=1. This approach makes use of the internal numpy library `np.roll` which makes it lot easier to get the desired output.

```bash
def roll_np_array(arr, shift, axis=0):
    """
    This function rolls the numpy array based
    on shift value and axis provided.
    """
    return np.roll(arr, shift, axis=axis)
```

