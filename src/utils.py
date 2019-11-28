# Import libraries
import json
import numpy as np


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


def get_unique_items(array):
    """
    This function gets the unique items
    from the provided numpy array.
    """
    unique_items = np.unique(array)
    return unique_items


def to_output_array(array):
    """
    This function copied the provided numpy
    array to another array.
    """
    cloned_array = np.copy(array)
    return cloned_array


def get_shape_of_array(array):
    """
    This function returns the shape of the
    numpy array.
    """
    n_row, n_column = np.shape(array)
    return n_row, n_column


def compare_np_array(arr1, arr2):
    """
    This function compares the two numpy array
    and returns the bool response.
    """
    return np.array_equal(arr1, arr2)


def output_to_json(arr):
    """
    This function converts the provided numpy
    array to json object and returns back.
    """
    return json.dumps({'output': arr.tolist()})


def roll_np_array(arr, shift, axis=0):
    """
    This function rolls the numpy array based
    on shift value and axis provided.
    """
    return np.roll(arr, shift, axis=axis)
