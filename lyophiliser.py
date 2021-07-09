"""
TODO:
    1.legend
    2.plot time on x axis

"""

import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.colors as colors


# Parameters
x_len = 200         # Number of points to display
temp_range = [-50, 40]  # Range of possible Y1 values to display
pressure_range = [0, 110]  # Range of possible Y2 values to display

# Create figure for plotting
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
# Adding Twin Axes to plot using dataset_2
ax2 = ax1.twinx() 

xs = list(range(0, 200))
y1s = [0] * x_len
y2s = [0] * x_len
y3s = [0] * x_len
ax1.set_ylim(temp_range)
ax2.set_ylim(pressure_range)


# Create a blank line. We will update the line in animate
line1, = ax1.plot(xs, y1s,color = 'navy')
line2, = ax1.plot(xs, y2s,color = 'lightskyblue')
line3, = ax2.plot(xs, y3s,color = 'm')

line1.set_label('Lyophiliser Temperature')
line2.set_label('Condenser Temperature')
line3.set_label('System Pressure')


# Add axis labels
plt.title('Real time Lyophiliser Data')
ax1.set_xlabel("Samples")

ax1.set_ylabel("Temperature / degC", color = 'navy')
ax1.tick_params(axis ='y', labelcolor = 'navy')

ax2.set_ylabel("Pressure / kPa",color='m')
ax2.tick_params(axis ='y', labelcolor = 'm')





# This function is called periodically from FuncAnimation
def animate(i, y1s,y2s,y3s):

    # Read temperature (Celsius) from lyophilisation chamber
    temp_lyo = round(25, 2)
    # Read temperature (Celsius) from condenser
    temp_condenser = round(28, 2)
    # Read pressure (kPa) from sensor
    pressure_system = round(24, 2)
    
    # Add y to list
    y1s.append(temp_lyo)
    y2s.append(temp_condenser)
    y3s.append(pressure_system)

    # Limit y list to set number of items
    y1s = y1s[-x_len:]
    y2s = y2s[-x_len:]
    y3s = y3s[-x_len:]

    # Update line with new Y values
    line1.set_ydata(y1s)
    line2.set_ydata(y2s)
    line3.set_ydata(y3s)
    
    ax1.legend()
    ax2.legend()

    return line1,line2, line3

# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig,
    animate,
    fargs=(y1s,y2s,y3s),
    interval=50,
    blit=True)
plt.show()
