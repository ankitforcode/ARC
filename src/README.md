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

Each solution involves the json file to be provided as input for the execution and desired output is acheived.  

## Code Execution

1. The first approach to the solution involves shifting the numpy array on axis=1. This approach makes use of the internal numpy library `np.roll` which makes it lot easier to get the desired output.

```bash
def roll_np_array(arr, shift, axis=0):
    """
    This function rolls the numpy array based
    on shift value and axis provided.
    """
    return np.roll(arr, shift, axis=axis)
```

