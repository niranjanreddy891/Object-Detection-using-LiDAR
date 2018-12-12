import numpy as np
import random
import scipy as sc
from laspy import file
import pcl
from pcl import pcl_visualization
import tkinter
import tkinter as tk
from tkinter.filedialog import askopenfilename
import tensorflow as tf
import keras

def browseFile1():
  global inFile1
  inFile1=askopenfilename()
  txt1.insert(0.0, inFile1)
root = tk.Tk()
root.title("Visualization tool")
Label = tk.Label(root, text="Select a LAS file")
Label.grid(row = 1, column = 0, columnspan = 30)


browseButton1 = tk.Button(root,text="Browse", command=browseFile1)
browseButton1.grid(row = 2, column = 2)

txt1 = tk.Text(root, width = 60, height = 1)
txt1.grid(row = 2, column = 0, columnspan = 2)

def on_click():
    f = file.File(inFile1,mode='r')
    ptcloud = np.vstack((f.x, f.y, f.z)).transpose()
    f.close()

    # Centred the data
    ptcloud_centred = ptcloud - np.mean(ptcloud, 0)

    # Simulate an intensity information between 0 and 1
    ptcloud_centred = sc.append(ptcloud_centred, np.zeros((ptcloud.shape[0], 1)), axis=1)  # Ajout d'une ligne (axis=0)
    for i in range(ptcloud_centred.shape[0] - 1):
        ptcloud_centred[i, 3] = random.random()

    p = pcl.PointCloud_PointXYZI()
    p.from_array(np.array(ptcloud_centred, dtype=np.float32))

    visual = pcl_visualization.CloudViewing()
    visual.ShowGrayCloud(p)
    def check_was_stopped():
        visual.WasStopped()

        root.after(100, check_was_stopped)
    check_was_stopped()
#laspy librairy, read las file

label = tk.Label(root)
label.grid()

tk.Button(text="Visualize", command=on_click).grid()


root.geometry('600x130')
root.mainloop()
