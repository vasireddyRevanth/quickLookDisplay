import random
import tkinter as tk

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

from arduinoComm import echoMeasured
from datetime import datetime
import threading

import random
from itertools import count

import math


##################################

root = tk.Tk();
root.title("Quick Look Display");

ROOT_HEIGHT = root.winfo_height()
ROOT_WIDTH = root.winfo_width()
UPDATE_RATE =100   # in milliseconds

set1 = tk.DoubleVar()
set2 = tk.DoubleVar()
set3 = tk.DoubleVar()

root.minsize(1000,1000)

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

main_frame = tk.Frame(root, bg="red")
main_frame.grid(sticky="nsew")

main_frame.rowconfigure(0, weight =1);
main_frame.columnconfigure(0, weight=1);
main_frame.columnconfigure(1,weight=2);

left_frame = tk.Frame(main_frame, bg="green");
right_frame = tk.Frame(main_frame, bg="blue");

left_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10);
right_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10);


# Quadrants
right_frame.rowconfigure(0, weight=1)
right_frame.rowconfigure(1, weight=1)
right_frame.columnconfigure(0, weight=1)
right_frame.columnconfigure(1, weight=1)


set1_label = tk.Label(left_frame, text="Set X:", bg="green", foreground="white")
set1_label.grid(row=1, column=1, sticky="w")
set1_entry = tk.Entry(left_frame)
set1_entry.grid(row=1, column=2 )
set1_scale = tk.Scale(left_frame, variable=set1, from_ = 0, to=100000, orient=tk.HORIZONTAL, bg="green", foreground="white");
set1_scale.grid(row=1, column=3) 


set2_label = tk.Label(left_frame, text="Set X:", bg="green", foreground="white")
set2_label.grid(row=2, column=1, sticky="w")
set2_entry = tk.Entry(left_frame)
set2_entry.grid(row=2, column=2 )
set2_scale = tk.Scale(left_frame, variable=set2, from_ = 0, to=100000, orient=tk.HORIZONTAL, bg="green", foreground="white");
set2_scale.grid(row=2, column=3) 

set3_label = tk.Label(left_frame, text="Set X:", bg="green", foreground="white")
set3_label.grid(row=3, column=1, sticky="w")
set3_entry = tk.Entry(left_frame)
set3_entry.grid(row=3, column=2 )
set3_scale = tk.Scale(left_frame, variable=set3, from_ = 0, to=100000, orient=tk.HORIZONTAL, bg="green", foreground="white");
set3_scale.grid(row=3, column=3) 

set_button = tk.Button(left_frame, text="Submit")
set_button.grid(row=5, column=2 , columnspan=2)

measureX_label = tk.Label(left_frame, text="")
measureX_label.grid(row=1, column=4, padx="10")

measureY_label = tk.Label(left_frame, text="")
measureY_label.grid(row=2, column=4, padx="10")

measureZ_label = tk.Label(left_frame, text="")
measureZ_label.grid(row=3, column=4, padx="10")

measured= [];

plt.style.use('bmh')
# values for first graph
x = []
y1 = []
y2 = []
y3 = []
index = count()
index2 = count()


# values for first graph
x_vals = []
y_vals = []
z_vals = []

fig1, ax11 = plt.subplots()
fig2, ax12 = plt.subplots()
fig3, ax13 = plt.subplots()

measured = echoMeasured();

start_time = datetime.now()
time_elapsed = int()
def updateElapsedTime():
    global time_elapsed
    # Calculate the elapsed time
    elapsed_time = int((datetime.now() - start_time).total_seconds())
    
    # Print the elapsed time
    print(f"Elapsed time: {elapsed_time}")
    
    # Wait for 1 second before checking again
    time_elapsed = elapsed_time;

# Start a new thread to update the elapsed time
threading.Thread(target=updateElapsedTime, daemon=True).start()


def updateMeasured():
    global measured;
    measured = echoMeasured();
    current_time_str = datetime.now().strftime("%H:%M:%S");
    measureX_label.config(text=current_time_str);
    measureY_label.config(text=measured[1])
    measureZ_label.config(text=measured[2]);
    # generateGraph(measured[0], measured[1], measured[2]);


def animate():
    global measured
    # measured = echoMeasured()

    # Generate values
    x_vals.append(next(index))
    y_vals.append(math.sin(measured[1]))
    z_vals.append(measured[2])
    # Get all axes of figure
    # ax1, ax2, ax3 = plt.gcf().get_axes()
    # Clear current data

    ax11.clear()
    ax12.clear()
    ax13.clear()
    # Plot new data
    ax11.plot(x_vals, x_vals)
    ax12.plot(x_vals, y_vals)
    ax13.plot(x_vals, z_vals)
    # print(x_vals,"\n",y_vals,"\n", z_vals)


canvas1 = FigureCanvasTkAgg(fig1, master=right_frame)
canvas1.get_tk_widget().grid(column=0, row=1)
canvas2 = FigureCanvasTkAgg(fig2, master=right_frame)
canvas2.get_tk_widget().grid(column=0, row=2)
canvas3 = FigureCanvasTkAgg(fig3, master=right_frame)
canvas3.get_tk_widget().grid(column=1, row=1)

# Create two subplots in row 1 and column 1, 2
is_scheduled = True
def schedule_updates():
    schedule_duration=UPDATE_RATE; # in milliseconds

    global is_scheduled
    if is_scheduled:
        updateElapsedTime()
        updateMeasured()
        animate()
        # updateImage()
        root.after(schedule_duration, schedule_updates);




schedule_updates();
root.mainloop();
##################################

"""

def updateMeasured():
    measured = echoMeasured();
    measureX_label.config(text=measured[0]);
    measureY_label.config(text=measured[1]);
    measureZ_label.config(text=measured[2]);


plt.style.use('bmh')
x = [0]
y1= [0]
y2 = [0]
y3 = [0]
start_time = datetime.now()
time_elapsed = int()
def updateElapsedTime():
    global time_elapsed
    # Calculate the elapsed time
    elapsed_time = int((datetime.now() - start_time).total_seconds())
    
    # Print the elapsed time
    print(f"Elapsed time: {elapsed_time}")
    
    # Wait for 1 second before checking again
    time_elapsed = elapsed_time;
# Start a new thread to update the elapsed time
threading.Thread(target=updateElapsedTime, daemon=True).start()
def animate():
    # Generate values
    x.append(time_elapsed)
    y1.append(measured[0])
    y2.append(measured[1])
    y3.append(measured[2])
    # Get all axes of figure
    ax1, ax2, ax3 = plt.gcf().get_axes()
    # Clear current data
    ax1.cla()
    ax2.cla()
    ax3.cla()
    # Plot new data
    ax1.plot(x, y1)
    ax2.plot(x, y2)
    ax3.plot(x, y3)
canvas = FigureCanvasTkAgg(plt.gcf(), master=right_frame)
canvas.get_tk_widget().grid(column=0, row=1)
# Create two subplots in row 1 and column 1, 2
plt.gcf().subplots(1, 2)

# UPDATES

is_scheduled = True
def schedule_updates():
    schedule_duration=UPDATE_RATE; # in milliseconds

    global is_scheduled
    if is_scheduled:
        updateMeasured();
        ig();
        root.after(schedule_duration, schedule_updates);

ani = animation(plt.gcf(), animate, interval=100, blit=False)
plt.show()

schedule_updates()
root.mainloop()






index = count()
index2 = count()



    canvas = FigureCanvasTkAgg(plt.gcf(),master = right_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()
    toolbar = NavigationToolbar2Tk(canvas,root)
    toolbar.update()
    canvas.get_tk_widget().pack()

    # graph 1
    # canvas = FigureCanvasTkAgg(plt.gcf(), master=root)
    # canvas.get_tk_widget().grid(column=0, row=1)
    # Create two subplots in row 1 and column 1, 2
    plt.gcf().subplots(1, 2, 3)
    ani = animation(plt.gcf(), animate, interval=ROOT_HEIGHT, blit=False)


# GUI
root = Tk.Tk()
label = Tk.Label(root, text="Realtime Animated Graphs")


Tk.mainloop()


# for i in plt.style.available:
    # print(i)
"""