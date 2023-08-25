import time
from brainflow import BoardShim, BrainFlowInputParams, BoardIds

params = BrainFlowInputParams()
board = BoardShim(BoardIds.GANGLION_NATIVE_BOARD, params)
print("PENISSSSajslkdhaoS")
board.prepare_session()
print("PENISSSSS")
board.start_stream()
print("PENIS")
data = board.get_board_data()  # get all data and remove it from internal buffer
time.sleep(10)
print("PENIUS")

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
# Create a figure and axis for the live graph
fig, ax = plt.subplots()
lines_matrix = [
    [0],
    [0],
    [0],
    [0],
    [0]
]
lines_matrix_head = [
    [0],
    [0],
    [0],
    [0],
    [0]
]
# Convert the lines matrix to numpy arrays for easier manipulation
lines_matrix = [np.array(line) for line in lines_matrix]

# Initialize empty lines to be updated in the animation
lines = [ax.plot([], [], lw=2)[0] for _ in range(len(lines_matrix))]


# Set axis limits
ax.set_xlim(0, 20)
ax.set_ylim(-2e4, 2e4)
# Update function for the animation
def update(frame):
    global lines_matrix
    global lines_matrix_head
    # clear the axis
    ax.cla()
    to_add = board.get_current_board_data(1)
    print(to_add)
    for i in range(len(lines_matrix)):
        lines_matrix[i] = np.append(lines_matrix[i], to_add[i], axis=0)
        lines_matrix_head[i] = np.append(lines_matrix_head[i], to_add[i], axis=0)
    for i in range(len(lines_matrix)):
        # trim
        if len(lines_matrix[i]) > 100:
            lines_matrix[i] = lines_matrix[i][-100:]
        ax.plot(range(len(lines_matrix[i])), lines_matrix[i], lw=2)
    # freeze the axis
    ax.set_ylim(-2e4, 2e4)
    

# Create an animation
ani = FuncAnimation(fig, update, interval=10, repeat=True)

# Display the live graph
plt.show()
board.stop_stream()
board.release_session()
