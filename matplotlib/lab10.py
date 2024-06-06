import numpy as np
import scipy
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider
import matplotlib.ticker as mticker




def task1():
    X = np.linspace(-1, 1, 500)
    colors = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0), (1, 0, 1), (0, 1, 1), (0, 0, 0)]

    for i in range(7):
        plt.plot(X, scipy.special.legendre(i + 1)(X), color = colors[i], label = "n=" + str(i + 1))

    plt.legend()
    plt.title("Полиномы Лежандра")
    plt.show()



def task2():
    relations = [[[3, 2], [3, 4]], [[5, 4], [5, 6]]]
    figure, axes = plt.subplots(2, 2)
    T = np.linspace(0, 2 * np.pi, 1000)

    for i in range(2):
        for j in range(2):
            X = np.sin(relations[i][j][0] * T)
            Y = np.sin(relations[i][j][1] * T)

            axes[i][j].plot(X, Y)
            axes[i][j].set_title("Relation: " + str(relations[i][j][0]) + ":" + str(relations[i][j][1]))
    
    plt.tight_layout()
    plt.show()


def task3():
    relation = [3, 2]

    def update_Lissajous(frame, line):
        line.set_data(np.sin(relation[0] * T + frame), np.sin(relation[1] * T + frame))
        return [line]
    
    figure, axis = plt.subplots()
    T = np.linspace(0, 2 * np.pi, 1000)
    X = np.sin(relation[0] * T)
    Y = np.sin(relation[1] * T)

    line, = axis.plot(X, Y)
    phasa = np.linspace(0, 4 * np.pi, 100)

    animation = FuncAnimation(
        figure, 
        func = update_Lissajous,
        frames = phasa, 
        fargs = (line,),
        interval = 30,
        blit = True,
        repeat = True
    )

    plt.show()



def task4():
    def function(x, amplitude, frequency):
        return amplitude * np.sin(2 * np.pi * frequency * x)

    X = np.linspace(0, 1, 1000)

    amplitude_on_start = 5
    frequency_on_start = 3

    figure, axes = plt.subplots(3)
    line1, = axes[0].plot(X, function(X, amplitude_on_start, frequency_on_start))
    line2, = axes[1].plot(X, function(X, amplitude_on_start, frequency_on_start))

    line_sum, = axes[2].plot(X, 2 * function(X, amplitude_on_start, frequency_on_start))

    figure.subplots_adjust(bottom = 0.4)

    axfreq1 = figure.add_axes([0.2, 0.32, 0.65, 0.03])
    freq_slider1 = Slider(
        ax=axfreq1,
        label='Frequency 1',
        valmin=0.1,
        valmax=30,
        valinit=frequency_on_start
    )
    axfreq2 = figure.add_axes([0.2, 0.16, 0.65, 0.03])
    freq_slider2 = Slider(
        ax=axfreq2,
        label='Frequency 2',
        valmin=0.1,
        valmax=30,
        valinit=frequency_on_start
    )
    axamp1 = figure.add_axes([0.2, 0.24, 0.65, 0.03])
    amp_slider1 = Slider(
        ax=axamp1,
        label="Amplitude 1",
        valmin=0,
        valmax=10,
        valinit=amplitude_on_start
    )
    axamp2 = figure.add_axes([0.2, 0.08, 0.65, 0.03])
    amp_slider2 = Slider(
        ax=axamp2,
        label="Amplitude 2",
        valmin=0,
        valmax=10,
        valinit=amplitude_on_start
    )


    def update(val):
        line1.set_ydata(function(X, amp_slider1.val, freq_slider1.val))
        line2.set_ydata(function(X, amp_slider2.val, freq_slider2.val))
        line_sum.set_ydata(function(X, amp_slider1.val, freq_slider1.val) + function(X, amp_slider2.val, freq_slider2.val))
        figure.canvas.draw_idle()


    freq_slider1.on_changed(update)
    amp_slider1.on_changed(update)
    freq_slider2.on_changed(update)
    amp_slider2.on_changed(update)

    plt.show()
    



def task5():
    def log_tick_formatter(val, pos = None):
        return "10^" + str(int(val))
    
    X = np.linspace(-10, 10, 100)
    Y = np.linspace(-10, 10, 100)
    X, Y = np.meshgrid(X, Y)
    F = (X ** 2 + Y ** 2) / 2

    fig = plt.figure()
    
    ax1 = fig.add_subplot(121, projection='3d')
    ax1.plot_wireframe(X, Y, F)
    ax1.set_xlabel('X')
    ax1.set_ylabel('Y')
    ax1.set_zlabel('Z')
    ax1.set_title('MSE Surface Plot')

    
    ax2 = fig.add_subplot(122, projection='3d')
    ax2.plot_wireframe(X, Y, np.log10(F))
    ax2.set_xlabel('X')
    ax2.set_ylabel('Y')
    ax2.set_zlabel('Z')
    ax2.zaxis.set_major_formatter(mticker.FuncFormatter(log_tick_formatter))
    ax2.set_title('MSE Surface Plot (Log Scale)')
    
    
    plt.show()


# task1()
# task2()
# task3()
# task4()
task5()