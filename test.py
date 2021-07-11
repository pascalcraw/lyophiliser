import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import matplotlib.colors as colors #allows additioinal colour names to be used (for graphing)


fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
# Adding Twin y Axes to plot
ax2 = ax1.twinx()

temp_range = [-80, 60]  # Range of possible Y1 values to display
pressure_range = [0, 140]  # Range of possible Y2 values to display

# Add axis labels
plt.title('Real time Lyophiliser Data')


def animate(i):
    graph_data = open('lyophiliser_run_file.txt','r').read()
    lines = graph_data.split('\n')
    xs = []
    y1s = []
    y2s = []
    y3s = []

    for line in lines:
        if len(line) > 1:
            x, y1,y2,y3 = line.split(',')

            # Add y to list
            xs.append(float(x))
            y1s.append(float(y1))
            y2s.append(float(y2))
            y3s.append(float(y3))

    ax1.clear()

    ax1.set_ylim(temp_range)
    ax2.set_ylim(pressure_range)
    ax1.set_xlabel("Samples")
    ax1.set_ylabel("Temperature / degC", color='navy')
    ax2.set_ylabel("Pressure / kPa", color='m')
    ax1.tick_params(axis='y', labelcolor='navy')
    ax2.tick_params(axis='y', labelcolor='m')
    ax1.set_facecolor('lightgrey')
    ax1.grid(which='both')
    ax1.grid(which='minor', alpha=0.2, linestyle='--')
    ax1.plot(xs, y1s, color='navy', label='Lyophiliser Temperature')
    ax1.plot(xs, y2s, color='lightskyblue', label='Condenser Temperature')
    ax2.plot(xs, y3s, color='m', label='System Pressure')


# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig, animate, interval=1000)

plt.show()