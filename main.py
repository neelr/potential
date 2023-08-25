import time
from brainflow import BoardShim, BrainFlowInputParams, BoardIds
import numpy as np
from tools import storage

print(storage.get_storage_path())
params = BrainFlowInputParams()
board = BoardShim(BoardIds.GANGLION_NATIVE_BOARD, params)

board.prepare_session()
board.start_stream()

def startRecordingSample(name, seconds):
    global board
    board.get_board_data()
    for i in range(seconds): # samples 200 times per second
        time.sleep(1)
        print(f"Sample end in {seconds-i}")
    data = board.get_board_data()
    print(f"Sample {name} recorded, shape: {data.shape}")
    storage.storeEEGData(data, name)
    print("waiting for 5 seconds")
    time.sleep(5)

print("waiting for 5 seconds")
time.sleep(5)
startRecordingSample("squeeze1", 30)
startRecordingSample("rest1", 30)
startRecordingSample("squeeze2", 30)
startRecordingSample("rest2", 30)
startRecordingSample("squeeze3", 30)
startRecordingSample("rest3", 30)
startRecordingSample("squeeze4", 30)
startRecordingSample("rest4", 30)
startRecordingSample("squeeze5", 30)
startRecordingSample("rest5", 30)

board.stop_stream()
board.release_session()