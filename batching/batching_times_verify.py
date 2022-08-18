import numpy as np
import time
import math
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from batching_times import get_room_for_error

h = 10
g = 32
w = 40


def plot_demo(batch_delay, ends_delay, ax):
    batch_count = math.ceil((w+ends_delay) / batch_delay) + 1
    y = 0
    for i in range(batch_count):
        ws = batch_delay * i
        we = ws + w
        ge = we - ends_delay
        gs = ge - g
        he = ge - ends_delay
        hs = he - h
        ax.plot((ws, we), (y, y), (0,0), linewidth=4, color='purple')
        y -= 3
        ax.plot((gs, ge), (y, y), linewidth=4, color='b')
        y -= 3
        ax.plot((hs, he), (y, y), linewidth=4, color='g')
        y -= 3
        ax.axvspan(he, we, alpha=0.2, color='red')
        y -= 2

def update(val=0):
    ax.cla()
    plot_demo(slider.val, slider2.val, ax)
    room_for_error = get_room_for_error(slider.val, slider2.val)
    if room_for_error == 0:
        ax.set_title('Invalid')
    else:
        ax.set_title(f'Room for error = {room_for_error:.2f}')

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.35)

ax_slider = plt.axes([0.25, 0.15, 0.65, 0.03])
ax_slider2 = plt.axes([0.25, 0.05, 0.65, 0.03])

slider = Slider(
    ax=ax_slider,
    label='Batch delay',
    valmin=1,
    valmax=40,
    valinit=7.14,
)

slider2 = Slider(
    ax=ax_slider2,
    label='Ends delay',
    valmin=0.01,
    valmax=10,
    valinit=1.2,
)

slider.on_changed(update)
slider2.on_changed(update)

update()

plt.show()
