import csv
import datetime as dt
import time
import tkinter as tk
from threading import Event, Thread
from tkinter import *
from tkinter import messagebox

import matplotlib
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

#import TThread

matplotlib.use("TkAgg")

win = tk.Tk()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Define fonts~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

LARGE_FONT = ('Verdane', 12)
MID_FONT = ('Verdane', 10)
SMALL_FONT = ('Verdane', 8)

style.use("ggplot")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Define graph sizes and location~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

fig = Figure(figsize=(10,5), dpi=100)
TempPlt = fig.add_subplot(221)
O2Plt = fig.add_subplot(222)
pHPlt = fig.add_subplot(212)

#|||||||||||||||||||||||||||||||||||||| Classes ||||||||||||||||||||||||||||||||||||||||||||||||||||||||

class WaterMS(tk.Tk):
    def __init__(self, *args , **kwargs):

        # This section intialises frames for the User Interface

        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, 'Water Monitoring System')
        
        container = tk.Frame(self)
        container.pack(side = 'top', fill='both', expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
        #Container is the parameter which the frame is going to be

        self.frames = {}
        
        for i in (Settings,Graphs):
            frame = i(container, self)
            self.frames[i] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            self.show_frame(i)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        # show_frame will display the window 

    def Run_Create(self):
        self.Create_Spinbox()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Settings(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = 'Settings Menu',
             font = LARGE_FONT)
        label.grid(column = 0, row = 0)
        self.Setting_Store = {'Max Temperature': 35,
                                'Min Temperature': 15,
                                'Temperature Spike Range' : 10,
                                'pH Spike Range' : 2,
                                'Max pH': 8,
                                'Min pH': 6}
        print(self.Setting_Store)

        

        #Declare values for spinbox
        self.RangeMin = [-20,-19,-18,-17,-16,-15,-14,-13,-12,-11,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1
                        ,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

        #Declare spinbox
        self.spinTemp1 = IntVar()
        self.spinTempMin = IntVar()
        self.spinTempMax = IntVar()
        self.spin_pH = IntVar()
        self.spin_pHMax = IntVar()
        self.spin_pHMin = IntVar()

        #Get values from spin box
        self.TempMax = self.spinTempMax.get()
        self.TempMin = self.spinTempMin.get()
        self.TempSpike = self.spinTemp1.get()
        self.pHSpike = self.spin_pH.get()
        self.pHMax = self.spin_pHMax.get()
        self.pHMin = self.spin_pHMin.get()
        
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Show Graph Button~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        self.ShowButton = tk.Button(self, text = "Show Graph", command = lambda : controller.show_frame(Graphs))
        self.ShowButton.grid(column = 3, row = 11)

        self.Create_Spinbox()


    def Create_Spinbox(self):
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Procedure to Store Settings~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        def Store_values():
            self.Setting_Store['Max Temperature'] = self.TempMax
            self.Setting_Store['Min Temperature'] = self.TempMin
            self.Setting_Store['Temperature Spike Range'] = self.TempSpike
            self.Setting_Store['pH Spike Range'] = self.pHSpike
            self.Setting_Store['Max pH'] = self.pHMax
            self.Setting_Store['Min pH'] = self.pHMin
            
            self.SaveData = [self.Setting_Store['Max Temperature'], self.Setting_Store['Min Temperature'],
            self.Setting_Store['Temperature Spike Range'],self.Setting_Store['pH Spike Range'],
            self.Setting_Store['Max pH'],self.Setting_Store['Min pH']]

            with open('Settings_Info', 'r+') as file:
                file.truncate(0)
                file.write(self.SaveData)
                file.close()
                print(file)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Temp Spinbox~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        
        #Creates spinbox
        self.spinTemp1 = tk.Spinbox(self, from_=0, to=20, width = 5)
        self.spinTemp1.grid(column=0, row=3)
        
        #Label spinbox
        labelSpinTemp =  tk.Label(self, text = 'Temperature Spike Range', font = MID_FONT)
        labelSpinTemp.grid(column = 0, row = 2, columnspan = 3)
        

        self.spinTempMin = tk.Spinbox(self, value = self.RangeMin, width = 5)
        self.spinTempMin.grid(column=0, row=5)

        labelSpinTemp1 =  tk.Label(self, text = 'Minimum Temperature', font = MID_FONT)
        labelSpinTemp1.grid(column = 0, row = 4, columnspan = 3)

        self.spinTempMax = tk.Spinbox(self, from_= 20, to= 45, width = 5)
        self.spinTempMax.grid(column=0, row=7)

        labelSpinTemp2 =  tk.Label(self, text = 'Maximum Temperature', font = MID_FONT)
        labelSpinTemp2.grid(column = 0, row = 6, columnspan = 3)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~pH Spinbox~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        self.spin_pH = tk.Spinbox(self, from_= 0, to= 5, width = 5)
        self.spin_pH.grid(column= 5, row=3)
        
        labelSpinpH =  tk.Label(self, text = 'pH spike range', font = MID_FONT)
        labelSpinpH.grid(column = 5 , row = 2, columnspan = 6)

        self.spin_pHMax = tk.Spinbox(self, from_= 6, to= 12, width = 5)
        self.spin_pHMax.grid(column=5, row=5)

        labelSpinpH1 =  tk.Label(self, text = 'Maximum pH', font = MID_FONT)
        labelSpinpH1.grid(column = 5, row = 4, columnspan = 3)

        self.spin_pHMin = tk.Spinbox(self, from_= 0, to= 6, width = 5)
        self.spin_pHMin.grid(column=5, row=7)

        labelSpinpH2 =  tk.Label(self, text = 'Minimum pH', font = MID_FONT)
        labelSpinpH2.grid(column = 5, row = 6, columnspan = 3)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Save Button~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        saveButton = tk.Button(self, text = "Save", command = Store_values)
        saveButton.grid(column = 3, row = 10)

class Graphs(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = 'Live Graph',
             font = LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Back to Settings",
                            command=lambda: controller.show_frame(Settings))
        button1.pack()
        
        self.Create_Graph()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Define each Graph~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def animateTemp(self, i):
        collectData = open('Temperature.csv','r').read()
        dataArray = collectData.split('\n')

        Temp_Input=[]
        Time_Input=[]
        for eachLine in dataArray:
            if len(eachLine)>1:
                y,temp = eachLine.split(',')
                x = [datetime.datetime.now() + datetime.timedelta(hours=i) for i in range(len(y))]
                Time_Input.append(x)
                Temp_Input.append(float(y))

        TempPlt.clear()
        TempPlt.plot(Time_Input,Temp_Input)

    def animatepH(self, i):
        collectData = open('ph.csv','r').read()
        dataArray = collectData.split('\n')

        pH_Input=[]
        Time_Input=[]
        for eachLine in dataArray:
            if len(eachLine)>1:
                y,temp = eachLine.split(',')
                x = [datetime.datetime.now() + datetime.timedelta(hours=i) for i in range(len(y))]
                Time_Input.append(x)
                pH_Input.append(float(y))

        pHPlt.clear()
        pHPlt.plot(Time_Input,pH_Input)

    def animateO2(self, i):
        collectData = open('o2.csv','r').read()
        dataArray = collectData.split('\n')

        O2_Input=[]
        Time_Input=[]
        for eachLine in dataArray:
            if len(eachLine)>1:
                y,temp = eachLine.split(',')
                x = [datetime.datetime.now() + datetime.timedelta(hours=i) for i in range(len(y))]
                Time_Input.append(x)
                O2_Input.append(float(y))


        O2Plt.clear()
        O2Plt.plot(Time_Input,O2_Input)

    def Create_Graph(self):
        self.TempPlt = fig.add_subplot(221)
        self.O2Plt = fig.add_subplot(222)
        self.pHPlt = fig.add_subplot(212)

        canvas = FigureCanvasTkAgg(fig, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.ani = animation.FuncAnimation(fig, self.animateTemp, frames=100,interval=100)
        self.ani2 = animation.FuncAnimation(fig, self.animatepH, frames=100,interval=100)
        self.ani3 = animation.FuncAnimation(fig, self.animateO2, frames=100,interval=100)

class PopUp(tk.Frame):
    
    extra = tk.Tk()
    extra.withdraw()
    def __init__(self,parent):
        #Declare what type of error
        self.ErrorCode = False
        self.WhatFault = ""

        #Declare what typr of anomaly or spike
        self.ChangeCode = False
        self.WhatChanged = ""

        #This is for when values are constant over a period 
        self.TypeOfError = {"TempError" : "Temperature Sensor Fault \n Click Okay",
                            "O2Error" : "Oxygen Dissolver Fault \n Click Okay",
                            "pHError" : "pH Sensor Fault \n Click Okay"}

        #This is for when a spike or anomaly occurs
        self.VarChanged = {"Temp": "Temperature has Spiked or has gone out of acceptance range \n Click Okay",
                           "pH": "pH has Spiked or has gone out of acceptance range \n Click Okay",
                           "O2": "O2 has Spiked or has gone out of acceptance range \n Click Okay", }

        self.TCalcData()
        self.PCalcData()

    def TCalcData(self):
        collectData = open('Temperature.csv','r').read()
        dataArray = collectData.split('\n')

        for eachLine in dataArray:
            if len(eachLine)>1:
                y,x,Data = eachLine.split(',')
                if Data == 'Anomaly' or Data == 'Spike':
                    self.WhatChanged = 'Temp'
                    self.ChangeCode = True
                    self.ShowBox()

    
    def PCalcData(self):
        collectData = open('ph.csv','r').read()
        dataArray = collectData.split('\n')

        for eachLine in dataArray:
            if len(eachLine)>1:
                y,x,Data = eachLine.split(',')
                if Data == 'Anomaly' or Data == 'Spike':
                    self.WhatChanged = 'Temp'
                    self.ChangeCode = True
                    self.ShowBox()

    def ShowBox(self):
        # This procedure determines which meesage box to pop up
        if self.ErrorCode == True:
            CurrentVal = self.TypeOfError[self.WhatFault]
            messagebox.showwarning("Error", CurrentVal)

        elif self.ChangeCode == True:
            TypeVal = self.VarChanged[self.WhatChanged]
            messagebox.showwarning("Error", TypeVal)

Window = WaterMS()
Window.mainloop()
