import json
import numpy as np


def load_json(filename):
    """
    This function takes the filename as imput and 
    laods the jsobn object in a variables and 
    returns back.
    """
    with open(filename) as json_file:
        data = json.load(json_file)
    return data


def to_numpy_array(array):
    """
    This function converts the list type to numpy
    array for further processing of the data.
    """
    arr = np.array(array)
    return arr


def find_unique(array):
    return np.unique(array)


def to_output_array(array):
    return np.copy(array)
