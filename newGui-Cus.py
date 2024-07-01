import random
import tkinter as tk
import customtkinter as Ctk

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

from arduinoComm import echoMeasured, send_data
from datetime import datetime
import threading

import random
from itertools import count

import math
from numpy import clip

# =============================================


root = tk.Tk();
root.title("Quick Look Display");

ROOT_HEIGHT = root.winfo_height()
ROOT_WIDTH = root.winfo_width()
UPDATE_RATE =100   # in milliseconds
ANIMATE_RATE =1000   # in milliseconds

setX = tk.DoubleVar()
setY = tk.DoubleVar()
setZ = tk.DoubleVar()


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
setX_label = Ctk.CTkLabel(input_frame, text="Reset: ", font=('Roboto', 20))
setX_label.grid(row=0, column=1, sticky="w", padx=12, pady=12)
# =============================================


# ================ Set Func ===================
def set_clamp(dVar):
    clamped = clip(dVar.get(), a_min=0, a_max=100000);
    dVar.set(clamped);

def set_values():

    set_clamp(setX);
    setX_push.configure(text=f"X: {setX.get()}")

    set_clamp(setY);
    setY_push.configure(text=f"Y: {setY.get()}")

    set_clamp(setZ);
    setZ_push.configure(text=f"Z: {setZ.get()}")

    send_set_values(setX.get(), setY.get(), setZ.get());

def reset(set_variable):
    set_variable.set(0.0);
# =============================================


# =================== Set 1 ===================
setX_label = Ctk.CTkLabel(input_frame, text="X:", font=('Roboto', 17))
setX_label.grid(row=1, column=1, sticky="w", padx=13, pady=12)

setX_entry = Ctk.CTkEntry(input_frame, placeholder_text ="X Value (T)", corner_radius=10, textvariable=setX);
setX_entry.grid(row=1, column=2 , padx=10, pady=10)

setX_slider = Ctk.CTkSlider(input_frame,from_=0,to=100000, variable=setX, number_of_steps=100000);
setX_slider.grid(row=2, column=1, columnspan=3, padx=10, pady=10)

resetX_button = Ctk.CTkButton(input_frame, text="Reset X", command=lambda: reset(setX), width=100);
resetX_button.grid(row=1, column=3 , columnspan=2, padx=10, pady=10)

setX_push = Ctk.CTkLabel(input_frame, text="X: 0.0", font=('Roboto', 17))
setX_push.grid(row=1, column=5, sticky="w", padx=25, pady=12, rowspan=2);
# =============================================


# =================== Set 2 ===================
setY_label = Ctk.CTkLabel(input_frame, text="Y:", font=('Roboto', 17))
setY_label.grid(row=3, column=1, sticky="w", padx=13, pady=12)

setY_entry = Ctk.CTkEntry(input_frame, placeholder_text ="Y Value (T)", corner_radius=10, textvariable=setY);
setY_entry.grid(row=3, column=2 , padx=10, pady=10)

setY_slider = Ctk.CTkSlider(input_frame,from_=0,to=100000, variable=setY, number_of_steps=100000);
setY_slider.grid(row=4, column=1, columnspan=3, padx=10, pady=10); 

resetY_button = Ctk.CTkButton(input_frame, text="Reset Y", command=lambda: reset(setY), width=100)
resetY_button.grid(row=3, column=3 , columnspan=2, padx=10, pady=10)

setY_push = Ctk.CTkLabel(input_frame, text="Y: 0.0", font=('Roboto', 17))
setY_push.grid(row=3, column=5, sticky="w", padx=25, pady=12, rowspan=2);
# =============================================


# =================== Set 3 ===================
setZ_label = Ctk.CTkLabel(input_frame, text="Z:", font=('Roboto', 17))
setZ_label.grid(row=5, column=1, sticky="w", padx=13, pady=12)

setZ_entry = Ctk.CTkEntry(input_frame, placeholder_text ="Z Value (T)", corner_radius=10, textvariable=setZ);
setZ_entry.grid(row=5, column=2 , padx=10, pady=10)

setZ_slider = Ctk.CTkSlider(input_frame, from_=0, to=100000, variable=setZ, number_of_steps=100000);
setZ_slider.grid(row=6, column=1, columnspan=3, padx=10, pady=10); 

resetZ_button = Ctk.CTkButton(input_frame, text="Reset Z", command=lambda: reset(setZ), width=100)
resetZ_button.grid(row=5, column=3 , columnspan=2, padx=10, pady=10)

setZ_push = Ctk.CTkLabel(input_frame, text="Z: 0.0", font=('Roboto', 17))
setZ_push.grid(row=5, column=5, sticky="w", padx=25, pady=12, rowspan=2);
# =============================================


set_values_button = Ctk.CTkButton(input_frame, text="Set Values", command=set_values, width=200, height=45, font=('Roboto', 17));
set_values_button.grid(row=10,column=2,columnspan=5, padx=10,pady=20);


# ============= Measure Variables =============
measured_head_label = Ctk.CTkLabel(measured_frame, text="Measured:", font=("Roboto", 20))
measured_head_label.grid(row=0, column=0, padx="10.0", pady="10.0", rowspan=2);

measureX_label = Ctk.CTkLabel(measured_frame, text="X: 0", font=("Roboto", 17))
measureX_label.grid(row=2, column=0, padx="10.0", pady="10.0")

measureY_label = Ctk.CTkLabel(measured_frame, text="Y: 0", font=("Roboto", 17))
measureY_label.grid(row=3, column=0, padx="10.0", pady="10.0")

measureZ_label = Ctk.CTkLabel(measured_frame, text="Z: 0", font=("Roboto", 17))
measureZ_label.grid(row=4, column=0, padx="10.0", pady="10.0")
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
    root.after(1000,updateElapsedTime);

# Start a new thread to update the elapsed time
threading.Thread(target=updateElapsedTime, daemon=True).start()


def updateMeasured():
    global measured;
    measured = echoMeasured();
    try:
        current_time_str = datetime.now().strftime("%H:%M:%S");
        measureX_label.configure(text=f"X: {current_time_str}");
        measureY_label.configure(text=f"Y: {measured[1]}")
        measureZ_label.configure(text=f"Z: {measured[2]}");
        # generateGraph(measured[0], measured[1], measured[2]);
    except TypeError as e:
        print(e);
# anim1 = FuncAnimation(fig1, animate,interval=250, repeat=False)
# anim2 = FuncAnimation(fig2, animate,interval=250, repeat=False)
# anim3 = FuncAnimation(fig3, animate,interval=250, repeat=False)


# =============== Create graphs ===============
plt.style.use('ggplot');

fig1 = plt.Figure(figsize=(6,5), dpi=90)
ax11 = fig1.add_subplot(111);
fig2 = plt.Figure(figsize=(6,5), dpi=90)
ax21 = fig2.add_subplot(111);
fig3 = plt.Figure(figsize=(6,5), dpi=90)
ax31 = fig3.add_subplot(111);
# =============================================



canvas1 = FigureCanvasTkAgg(fig1, master=right_frame)
canvas1.get_tk_widget().grid(column=0, row=0)
canvas2 = FigureCanvasTkAgg(fig2, master=right_frame)
canvas2.get_tk_widget().grid(column=0, row=1)
canvas3 = FigureCanvasTkAgg(fig3, master=right_frame)
canvas3.get_tk_widget().grid(column=1, row=0)

cur_Time=0;

def animate():
    global ax11,ax12,ax13;
    global measured;
    global x_vals, y_vals, z_vals;
    global cur_Time,time_elapsed;
    measured = echoMeasured()
    if time_elapsed != cur_Time: 

        # Generate values
        x_vals.append(int(time_elapsed))
        y_vals.append(int(time_elapsed))
        z_vals.append(int(next(index)))

        # Slice for most recent 300 values
        x_vals = x_vals[-100:]
        y_vals = y_vals[-100:]
        z_vals = z_vals[-100:]
        
        ax11.cla();
        ax21.cla();
        ax31.cla();

        # Plot new data
        ax11.plot(x_vals, x_vals)
        ax21.plot(x_vals, y_vals)
        ax31.plot(x_vals, z_vals)

        canvas1.draw()   
        canvas2.draw()
        canvas3.draw()

        print(x_vals);
        time_elapsed = cur_Time;
        # root.after(ANIMATE_RATE, animate);


def send_set_values(setX,setY,setZ):
    print(f"!{setX}{setY}{setZ}#")
    # send_data(f"!{setX}{setY}{setZ}#");



threading.Thread(target=animate, daemon=True).start()
# animGraphs()

# plt.show()
# Create two subplots in row 1 and column 1, 2
is_scheduled = True
def schedule_updates():
    schedule_duration=UPDATE_RATE; # in milliseconds

    global is_scheduled
    if is_scheduled:
        updateMeasured()
        
        animate();
        # updateImage()
        root.after(1000, schedule_updates);




updateElapsedTime();
schedule_updates();
# animate();
root.mainloop();

# =============================================

"""

def updateMeasured():
    measured = echoMeasured();
    measureX_label.config(text=measured[0]);
    measureY_label.config(text=measured[1]);
    measureZ_label.config(text=measured[2]);


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
# ============X============X============X============X============X============X============X============X============X============

"""
def update_graph(canvas_id, data_list):

    # Assuming canvas_id is the global variable holding the canvas object
    fig = Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)
    ax.clear() # Clear the previous plot
    ax.plot(data_list)
    
    # Redraw the figure on the canvas
    canvas_id.draw()
    canvas_id.flush_events()




ax = fig1.add_subplot(111)
# line, = ax.plot(x, np.sin(x))



# canvas1.draw()

"""