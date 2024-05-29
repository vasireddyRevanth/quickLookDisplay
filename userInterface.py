import math
from datetime import datetime
import time
import threading

# import numpy as np
import matplotlib.pyplot as plt
from PIL import ImageTk, Image
from arduinoComm import echoMeasured
import tkinter as tk
#####


#####
UPDATE_RATE = 150 # Rate of display data updates (in miilliseconds)
GRAPH_PNG_PATH = 'graphs/';

root = tk.Tk()
root.title("SET values")

# Create the main frames
left_frame = tk.Frame(root, bg="white", width=1200)
right_frame = tk.Frame(root, bg="grey")

# Pack the main frames
left_frame.pack(side="left", fill="both", expand=True)
right_frame.pack(side="right", fill="both", expand=True)

#Quad1 (X)
quad1 = tk.Frame(right_frame)
# quad1.pack(side="left", fill="both", expand=True, padx=10, pady=10)
quad1.grid(row=0,column=0, padx=10, pady=10);

#Quad2 (Y)
quad2 = tk.Frame(right_frame)
# quad2.pack(side="right", fill="both", expand=True, padx=10, pady=10)
quad2.grid(row=0,column=2, padx=10, pady=10);

#Quad3 (Z)
quad3 = tk.Frame(right_frame)
# quad3.pack(side="right", fill="both", expand=True, padx=10, pady=10)
quad3.grid(row=1,column=0, padx=10, pady=10);

setValue = int();

set1_label = tk.Label(left_frame, text="Set X:")
set1_label.grid(row=0+4, column=0, sticky="w")
set1_scale = tk.Scale(left_frame, variable=setValue, from_ = 0, to=100000, orient=tk.HORIZONTAL);
set1_scale.grid(row=2+4, column=1) 

# set1_entry = tk.Entry(left_frame)
# set1_entry.grid(row=0+4, column=1)

set2_label = tk.Label(left_frame, text="Set Y:")
set2_label.grid(row=1+4, column=0, sticky="w")
set2_scale = tk.Scale(left_frame, variable=setValue, from_ = 0, to=100000, orient=tk.HORIZONTAL);
set2_scale.grid(row=2+5, column=1) 

# set2_entry = tk.Entry(left_frame)
# set2_entry.grid(row=1+4, column=1) 

set3_label = tk.Label(left_frame, text="Set Z:")
set3_label.grid(row=2+4, column=0, sticky="w") 
set3_scale = tk.Scale(left_frame, variable=setValue, from_ = 0, to=100000, orient=tk.HORIZONTAL);
set3_scale.grid(row=2+6, column=1) 

# set3_entry = tk.Entry(left_frame)
# set3_entry.grid(row=2+4, column=1) 


set_button = tk.Button(left_frame, text="Submit")
set_button.grid(row=3+4, columnspan=2)

measure1_label = tk.Label(left_frame, text="")
measure1_label.grid(row=0+4, column=2, sticky="w")

measure2_label = tk.Label(left_frame, text="")
measure2_label.grid(row=1+4, column=2, sticky="w")

measure3_label = tk.Label(left_frame, text="")
measure3_label.grid(row=2+4, column=2, sticky="w")

plotX_image_label = tk.Label(quad1)
plotY_image_label = tk.Label(quad2)
plotZ_image_label = tk.Label(quad3)


def updateImage():
    #X
    try:
        plotX_PATH = f"{GRAPH_PNG_PATH}graph-x.png"
        plotX_image_label.config(image="")
        plotX_open = Image.open(plotX_PATH)
        plotX_image = ImageTk.PhotoImage(plotX_open)
        plotX_image_label.config(image=plotX_image)
        plotX_image_label.image = plotX_image
        plotX_image_label.pack()
    except IOError:
        print(f"Failed to open image: {plotX_PATH}. Please check the file path and try again.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}");
        
    #Y
    try:
        plotY_PATH = f"{GRAPH_PNG_PATH}graph-y.png"
        plotY_image_label.config(image="")
        plotY_open = Image.open(plotY_PATH)
        plotY_image = ImageTk.PhotoImage(plotY_open)
        plotY_image_label.config(image=plotY_image)
        plotY_image_label.image = plotY_image
        plotY_image_label.pack()
    except IOError:
        print(f"Failed to open image: {plotY_PATH}. Please check the file path and try again.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}");
    
    #Z
    try:
        plotZ_PATH = f"{GRAPH_PNG_PATH}graph-z.png"
        plotZ_image_label.config(image="")
        plotZ_open = Image.open(plotZ_PATH)
        plotZ_image = ImageTk.PhotoImage(plotZ_open)
        plotZ_image_label.config(image=plotZ_image)
        plotZ_image_label.image = plotZ_image
        plotZ_image_label.pack()
    except IOError:
        print(f"Failed to open image: {plotZ_PATH}. Please check the file path and try again.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}");


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


x = [0]
y1= [0]
y2 = [0]
y3 = [0]


def generateGraph(m1,m2,m3):
    current_time_seconds = time_elapsed;
    x.append(current_time_seconds);
    y1.append(m1);
    y2.append(m2);
    y3.append(m3);
    
    #1
    plt.plot(x, y1)
    plt.savefig(f'{GRAPH_PNG_PATH}graph-x.png') 
    plt.close()
    
    #2
    plt.plot(x, y2)
    plt.savefig(f'{GRAPH_PNG_PATH}graph-y.png') 
    plt.close()

    #3
    plt.plot(x, y3)
    plt.savefig(f'{GRAPH_PNG_PATH}graph-z.png') 
    plt.close()

    
    print(x,"\n",y1)



# Measured Values
def updateMeasured():
    measured = echoMeasured();
    current_time_str = datetime.now().strftime("%H:%M:%S");
    measure1_label.config(text=current_time_str);
    measure2_label.config(text=measured[1])
    measure3_label.config(text=measured[2]);
    generateGraph(measured[0], measured[1], measured[2]);


# UPDATES

is_scheduled = True
def schedule_updates():
    schedule_duration=UPDATE_RATE; # in milliseconds

    global is_scheduled
    if is_scheduled:
        updateElapsedTime()
        updateMeasured()
        updateImage()
        root.after(schedule_duration, schedule_updates);



# Run the application

schedule_updates();

root.mainloop()
