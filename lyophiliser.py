"""
TODO:
   
    2.plot time on x axis
    3. add real 

"""

import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation  #allows graph realtime update
import matplotlib.colors as colors #allows additioinal colour names to be used (for graphing)
import numpy as np



# Parameters
x_len = 200         # Number of points to display
temp_range = [-80, 60]  # Range of possible Y1 values to display
pressure_range = [0, 140]  # Range of possible Y2 values to display

# Create figure for plotting
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
# Adding Twin y Axes to plot 
ax2 = ax1.twinx() 

xs = list(range(0, 200))
y1s = [0] * x_len
y2s = [0] * x_len
y3s = [0] * x_len
ax1.set_ylim(temp_range)
ax2.set_ylim(pressure_range)


ax1.grid(which='both')
ax1.grid(which='minor', alpha=0.2, linestyle='--')

# Create a blank line. We will update the line in animate
line1, = ax1.plot(xs, y1s,color = 'navy', label = 'Lyophiliser Temperature')
line2, = ax1.plot(xs, y2s,color = 'lightskyblue',label = 'Condenser Temperature')
line3, = ax2.plot(xs, y3s,color = 'm', label = 'System Pressure')


# Add axis labels
plt.title('Real time Lyophiliser Data')
ax1.set_xlabel("Samples")
ax1.set_ylabel("Temperature / degC", color = 'navy')
ax2.set_ylabel("Pressure / kPa",color='m')

ax1.tick_params(axis ='y', labelcolor = 'navy')
ax2.tick_params(axis ='y', labelcolor = 'm')

ax1.set_facecolor('lightgrey')



# This function is called periodically from FuncAnimation
def animate(i, y1s,y2s,y3s):

    # Read temperature (Celsius) from lyophilisation chamber
    temp_lyo = round(15, 2)
    # Read temperature (Celsius) from condenser
    temp_condenser = round(18, 2)
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
    
    # ask matplotlib for the plotted objects and their labels
    lines, labels = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    plt.legend(lines + lines2, labels + labels2, edgecolor = 'black')
    #ax1.legend()
    

    return line1,line2, line3

# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig,
    animate,
    fargs=(y1s,y2s,y3s),
    interval=50,
    blit=True)
plt.show()
