# import serial 
# from arduinoComm import echoMeasured, read_buffer, extract_messages
# from datetime import datetime
# import cProfile
# import threading


# T =60;
# try:
#     while T>0:
#         print(echoMeasured(), datetime.now().strftime("%H:%M:%S"));
#         # cProfile.run('echoMeasured()');
#         T-=1;


# except KeyboardInterrupt:
#     print("\nCaught KeyboardInterrupt")

#     # Open the serial port 

import random
import tkinter as Tk
from itertools import count

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

plt.style.use('fivethirtyeight')
# values for first graph
x_vals = []
y_vals = []
# values for second graph
y_vals2 = []
y_vals3 = []


index = count()
index2 = count()

def animate(i):
    # Generate values
    x_vals.append(next(index))
    y_vals.append(random.randint(0, 5))
    y_vals2.append(random.randint(0, 5))
    y_vals3.append(random.randint(0, 5))

    # Get all axes of figure
    ax1, ax2 = plt.gcf().get_axes()
    ax3 = plt.gcf().get_axes()
    # Clear current data
    ax1.cla()
    ax2.cla()
    ax3.clear()

    # Plot new data
    ax1.plot(x_vals, y_vals)
    ax2.plot(x_vals, y_vals2)
    ax3.plot(x_vals, y_vals3)

# GUI
root = Tk.Tk()
label = Tk.Label(root, text="Realtime Animated Graphs").grid(column=0, row=0)

# graph 1
canvas = FigureCanvasTkAgg(plt.gcf(), master=root)
canvas.get_tk_widget().grid(column=0, row=1)
# Create two subplots in row 1 and column 1, 2
plt.gcf().subplots(1, 2)
ani = FuncAnimation(plt.gcf(), animate, interval=1000, blit=False)

Tk.mainloop()