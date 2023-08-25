import os
import pickle
import logging
import datetime


def get_storage_path():
    return os.path.join(os.path.dirname(os.path.dirname(__file__)), 'cache')

def storeEEGData(data, filename='eeg_data.pkl'):
    """
    Stores the data in a file with the given filename
    """
    with open(os.path.join(get_storage_path(), f"{filename}-{datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.pkl"), 'wb') as f:
        pickle.dump(data, f)

def loadEEGData(filename='eeg_data.pkl'):
    """
    Loads the data from a file with the given filename
    """
    # check for file existence with any datetime appended
    for file in os.listdir(get_storage_path()):
        if file.startswith(filename):
            with open(os.path.join(get_storage_path(), file), 'rb') as f:
                return pickle.load(f)