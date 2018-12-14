import numpy as np
import random
import scipy as sc
from laspy import file
import tkinter
import tkinter as tk
from tkinter.filedialog import askopenfilename
import pclpy
from pclpy import pcl
from tkinter import *
import tensorflow as tf
import keras


def browseFile1():
  global inFile1
  inFile1=askopenfilename()
  txt1.insert(0.0, inFile1)
root = tk.Tk()
root.title("Selection of ROI")
Label = tk.Label(root, text="Select a LAS/LAZ file")    # both las and laz file support
Label.grid(row = 1, column = 0, columnspan = 30)


browseButton1 = tk.Button(root,text="Browse", command=browseFile1)
browseButton1.grid(row = 2, column = 2)

txt1 = tk.Text(root, width = 80, height = 1)
txt1.grid(row = 2, column = 0, columnspan = 2)

def on_click():
    def ROI_window():
        offset = pclpy.io.las.get_offset(inFile1)
        pc = pclpy.io.las.read(inFile1, "PointXYZRGBA", xyz_offset=offset)
        viewer = pcl.visualization.PCLVisualizer("viewer", True)
        viewer.addPointCloud(pc)
        viewer.resetCamera()

        viewers = [viewer]

        def handle_event_area(event):
            # use x to toggle rectangle selection
            assert isinstance(event, pcl.visualization.AreaPickingEvent)
            indices = pcl.vectors.Int()
            event.getPointsIndices(indices)

            other_viewer = pcl.visualization.PCLVisualizer("viewer", True)
            rgb = np.array([pc.r[indices], pc.g[indices], pc.b[indices]]).T
            other_pc = pcl.PointCloud.PointXYZRGBA.from_array(pc.xyz[indices], rgb)
            other_viewer.addPointCloud(other_pc)
            other_viewer.resetCamera()
            viewers.append(other_viewer)

        viewer.registerAreaPickingCallback(handle_event_area)

        while not all(v.wasStopped() for v in viewers):
            for v in viewers:
                if not v.wasStopped():
                    v.spinOnce(50)

    ROI_window()


label = tk.Label(root)
label.grid()

tk.Button(text="Visualize", command=on_click).grid()


root.geometry('730x140')
root.mainloop()

#############################################################################

