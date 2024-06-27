import random
import tkinter as tk
import customtkinter as Ctk

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

from arduinoComm import echoMeasured
from datetime import datetime
import threading

import random
from itertools import count

import math


# =============================================


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

main_frame = Ctk.CTkFrame(root, border_width=5, border_color="red")
main_frame.grid(sticky="nsew")

main_frame.rowconfigure(0, weight =1);
main_frame.columnconfigure(0, weight=1);
main_frame.columnconfigure(1,weight=2);

left_frame = Ctk.CTkFrame(main_frame, border_width=5, border_color="green");
right_frame = Ctk.CTkFrame(main_frame, border_width=5, border_color="blue");

left_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10);
left_frame.rowconfigure(0,weight=2);
left_frame.rowconfigure(1,weight=3);
left_frame.columnconfigure(0,weight=1);
right_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10);

measured_frame = Ctk.CTkFrame(left_frame, border_width=5, border_color="purple");
measured_frame.grid(row = 0, column = 0, sticky="nsew", padx=10, pady=10, columnspan=5);


input_frame = Ctk.CTkFrame(left_frame, border_width=5, border_color="orange");
input_frame.grid(row = 1, column = 0, sticky="nsew", padx=10, pady=10);


# ============== Right Quadrants ==============
right_frame.rowconfigure(0, weight=1)
right_frame.rowconfigure(1, weight=1)
right_frame.columnconfigure(0, weight=1)
right_frame.columnconfigure(1, weight=1)
# =============================================


# ================== Set Head =================
set1_label = Ctk.CTkLabel(input_frame, text="Set: ", font=('Roboto', 20))
set1_label.grid(row=0, column=1, sticky="w", padx=12, pady=12)
# =============================================


# ================ Set Func ===================
def setX():
    set1_push.configure(text=f"X: {set1.get()}")
def setY():
    set2_push.configure(text=f"Y: {set2.get()}")
def setZ():
    set3_push.configure(text=f"Z: {set3.get()}")
# =============================================


# =================== Set 1 ===================
set1_label = Ctk.CTkLabel(input_frame, text="X:", font=('Roboto', 13))
set1_label.grid(row=1, column=1, sticky="w", padx=12, pady=12)

set1_entry = Ctk.CTkEntry(input_frame, placeholder_text ="X Value (T)", corner_radius=10, textvariable=set1);
set1_entry.grid(row=1, column=2 , padx=10, pady=10)

set1_slider = Ctk.CTkSlider(input_frame,from_=0,to=100000, variable=set1, number_of_steps=100000);
set1_slider.grid(row=2, column=1, columnspan=3, padx=10, pady=10)

set1_button = Ctk.CTkButton(input_frame, text="Set X", command=setX);
set1_button.grid(row=1, column=3 , columnspan=2, padx=10, pady=10)

set1_push = Ctk.CTkLabel(input_frame, text="X: ", font=('Roboto', 17))
set1_push.grid(row=1, column=5, sticky="w", padx=25, pady=12, rowspan=2);
# =============================================


# =================== Set 2 ===================
set2_label = Ctk.CTkLabel(input_frame, text="Y:", font=('Roboto', 13))
set2_label.grid(row=3, column=1, sticky="w", padx=12, pady=12)

set2_entry = Ctk.CTkEntry(input_frame, placeholder_text ="Y Value (T)", corner_radius=10, textvariable=set2);
set2_entry.grid(row=3, column=2 , padx=10, pady=10)

set2_slider = Ctk.CTkSlider(input_frame,from_=0,to=100000, variable=set2, number_of_steps=100000);
set2_slider.grid(row=4, column=1, columnspan=3, padx=10, pady=10); 

set2_button = Ctk.CTkButton(input_frame, text="Set Y", command=setY)
set2_button.grid(row=3, column=3 , columnspan=2, padx=10, pady=10)

set2_push = Ctk.CTkLabel(input_frame, text="Y: ", font=('Roboto', 17))
set2_push.grid(row=3, column=5, sticky="w", padx=25, pady=12, rowspan=2);
# =============================================


# =================== Set 3 ===================
set3_label = Ctk.CTkLabel(input_frame, text="Z:", font=('Roboto', 13))
set3_label.grid(row=5, column=1, sticky="w", padx=12, pady=12)

set3_entry = Ctk.CTkEntry(input_frame, placeholder_text ="Z Value (T)", corner_radius=10, textvariable=set3);
set3_entry.grid(row=5, column=2 , padx=10, pady=10)

set3_slider = Ctk.CTkSlider(input_frame, from_=0, to=100000, variable=set3, number_of_steps=100000);
set3_slider.grid(row=6, column=1, columnspan=3, padx=10, pady=10); 

set3_button = Ctk.CTkButton(input_frame, text="Set Z", command=setZ)
set3_button.grid(row=5, column=3 , columnspan=2, padx=10, pady=10)

set3_push = Ctk.CTkLabel(input_frame, text="Z: ", font=('Roboto', 17))
set3_push.grid(row=5, column=5, sticky="w", padx=25, pady=12, rowspan=2);
# =============================================


# ============= Measure Variables =============
measured_head_label = Ctk.CTkLabel(measured_frame, text="Measured:", font=("Roboto", 20))
measured_head_label.grid(row=0, column=0, padx="10", pady="10", rowspan=2);

measureX_label = Ctk.CTkLabel(measured_frame, text="X:", font=("Roboto", 15))
measureX_label.grid(row=2, column=0, padx="10", pady="10")

measureY_label = Ctk.CTkLabel(measured_frame, text="Y:", font=("Roboto", 15))
measureY_label.grid(row=3, column=0, padx="10", pady="10")

measureZ_label = Ctk.CTkLabel(measured_frame, text="Z:", font=("Roboto", 15))
measureZ_label.grid(row=4, column=0, padx="10", pady="10")
# =============================================



measured= [];

# plt.style.use('seaborn')
# values for first graph
x = []
y1 = []
y2 = []
y3 = []
index = count()
index2 = count()


# values for first graph
x_vals = [0]*300
y_vals = [0]*300
z_vals = [0]*300

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


def animate(i):
    global measured
    global x_vals, y_vals, z_vals
    measured = echoMeasured()

    # Generate values
    x_vals.append(next(index))
    y_vals.append(math.sqrt(measured[1]))
    z_vals.append(measured[2])
    # Get all axes of figure
    # ax1, ax2, ax3 = plt.gcf().get_axes()
    # Clear current data
    x_vals = x_vals[-300:]
    y_vals = y_vals[-300:]
    z_vals = z_vals[-300:]

    ax11.cla()
    ax12.cla()
    ax13.cla()
    # Plot new data
    ax11.plot(x_vals, x_vals)
    ax12.plot(x_vals, y_vals)
    ax13.plot(x_vals, z_vals)
    print(x_vals,"\n",y_vals,"\n", z_vals)



canvas1 = FigureCanvasTkAgg(fig1, master=right_frame)
canvas1.get_tk_widget().grid(column=0, row=1)
canvas2 = FigureCanvasTkAgg(fig2, master=right_frame)
canvas2.get_tk_widget().grid(column=0, row=2)
canvas3 = FigureCanvasTkAgg(fig3, master=right_frame)
canvas3.get_tk_widget().grid(column=1, row=1)


anim1 = FuncAnimation(fig1, animate,interval=250, repeat=False)
anim2 = FuncAnimation(fig2, animate,interval=250, repeat=False)
anim3 = FuncAnimation(fig3, animate,interval=250, repeat=False)


threading.Thread(target=animate, daemon=True).start()
# animGraphs()

# plt.show()
# Create two subplots in row 1 and column 1, 2
is_scheduled = True
def schedule_updates():
    schedule_duration=UPDATE_RATE; # in milliseconds

    global is_scheduled
    if is_scheduled:
        updateElapsedTime()
        updateMeasured()
        # animate()
        # updateImage()
        root.after(schedule_duration, schedule_updates);




# schedule_updates();
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
label = CTk.CTkLabel(root, text="Realtime Animated Graphs")


Tk.mainloop()


# for i in plt.style.available:
    # print(i)
"""