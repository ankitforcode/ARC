import json


def load_json(filename):
    """
    This function takes the filename as imput and 
    laods the jsobn object in a variables and 
    returns back.
    """
    with open(filename) as json_file:
        data = json.load(json_file)
    return data


# This is main handler for the proram
if __name__ == "__main__":
    data = load_json('25ff71a9.json')
    print(data)
    pass
