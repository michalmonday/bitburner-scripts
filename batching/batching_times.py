import numpy as np
import time
import math
import matplotlib.pyplot as plt

h = 10
g = 32
w = 40

plot_data = {
        'delays':[],
        'room_for_errors':[],
        'ends_delay':[]
        }

three_d = True

def start_offset_from_danger_zone_end(length, batch_delay):
    return batch_delay - length % batch_delay

def dist_from_danger_zone(offset, batch_delay, ends_delay):
    return max(0, min(offset, batch_delay - ends_delay*2 - offset))

def get_room_for_error(batch_delay, ends_delay):
    dze = w % batch_delay
    w_pos = start_offset_from_danger_zone_end(w, batch_delay)
    g_pos = start_offset_from_danger_zone_end(g + ends_delay, batch_delay)
    h_pos = start_offset_from_danger_zone_end(h + ends_delay*2, batch_delay)

    w_dist = dist_from_danger_zone(w_pos, batch_delay, ends_delay)
    g_dist = dist_from_danger_zone(g_pos, batch_delay, ends_delay)
    h_dist = dist_from_danger_zone(h_pos, batch_delay, ends_delay)
    room_for_error = max(0, min(h_dist, g_dist, w_dist))
    return room_for_error

for ends_delay in np.arange(0.01, h/7, 0.01):
    for batch_delay in np.arange(0.1, w/2, 0.1):
        room_for_error = get_room_for_error(batch_delay, ends_delay)
        plot_data['delays'].append(batch_delay)
        plot_data['room_for_errors'].append(room_for_error)
        plot_data['ends_delay'].append(ends_delay)


if __name__ == '__main__':

    if three_d:
        fig = plt.figure('comparison 3d')
        ax = plt.axes(projection='3d')
        ax.set_xlabel('Delay between batches')
        ax.set_ylabel('Delay between ends of H/G/W')
        ax.set_zlabel('Room for error')
        ax.scatter3D(plot_data['delays'], plot_data['ends_delay'], plot_data['room_for_errors'], c=plot_data['room_for_errors'], cmap='viridis', linewidth=0.5, edgecolor='black');

    else:
        plt.figure('comparison 2d') # (for a single "ends_delay")
        plt.scatter(plot_data['delays'], plot_data['room_for_errors'], c=plot_data['room_for_errors'], cmap='viridis', linewidth=0.5, edgecolor='black');

    plt.show()



