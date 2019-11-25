#Import libraries
import json
import os
import re
import numpy as np

class ProcessData():

    #init method or constructor
    def __init__(self, file):
        """
        These are set of initial variables that are 
        created when this class is initialized.
        """
        self.file = file
        self.filename = ""
        self.data = None
        self.input_grid = []
        self.test_grid = []
        self._get_json_file()
        self._load_json()
        self._get_grids_from_json()

    def _get_json_file(self):
        """
        This functions gets the json filename from the solution
        filename based on the realpath of current work dir.
        """
        dir_path = os.path.dirname(os.path.realpath(self.file))
        f = re.findall(r"[a-z0-9]+\w", self.file)[-2] + '.json'
        self.filename = dir_path + '/' + f

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
