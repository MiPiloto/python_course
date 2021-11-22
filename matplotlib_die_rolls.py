from matplotlib import animation
from math import sin
import matplotlib.pyplot as plt
import numpy as np
from numpy.core.fromnumeric import repeat
import seaborn as sns
import random

def update(frame_number, rolls, faces, frequencies):

    for i in range(rolls):
        frequencies[random.randrange(1, 7) - 1] += 1
        

    plt.cla()
    axes = sns.barplot(faces, frequencies, palette='bright')
    title = f'Die Frequencies for {sum(frequencies):,} Rolls'
    axes.set_title(title)
    axes.set(xlabel='Die Value', ylabel='Frequency')
    axes.set_ylim(top=max(frequencies) * 1.10)

    for bar, frequency in zip(axes.patches, frequencies):
        text_x = bar.get_x() + bar.get_width() / 2
        text_y = bar.get_height()
        text = f'{frequency:,}\n{frequency / sum(frequencies):.3%}'
        axes.text(text_x, text_y, text, fontsize=11, ha='center', va='bottom')

number_of_frames = 10000
rolls_per_frame = 600

sns.set_style('whitegrid')
figure = plt.figure('Rolling a six sided die')
values = list(range(1, 7))
frequencies = [0] * 6

die_animation = animation.FuncAnimation(
    figure, update, repeat=False, frames=number_of_frames, interval=33,
    fargs=(rolls_per_frame, values, frequencies))

plt.show()