import tkinter as tk
from tkinter import messagebox
import datetime
from datetime import time
import time as Time

class MySmartClock:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("900x500")
        self.root.title("Smart Clock")
        self.root.configure(bg="black")
        self.root.columnconfigure(0,weight=1)
        self.root.columnconfigure(1,weight=1)
        self.root.columnconfigure(2,weight=1)
        self.root.columnconfigure(3,weight=1)
        self.root.columnconfigure(4,weight=1)
        self.root.rowconfigure(0,weight=1)
        self.root.rowconfigure(1,weight=1)
        self.root.rowconfigure(2,weight=1)
        self.root.rowconfigure(3,weight=1)
        self.root.rowconfigure(4,weight=1)
        self.create_main_widgets()
        self.screen = "CurrentTime"
        self.detected_change = False
        self.check_state()
        
        self.root.mainloop()
        
    def create_main_widgets(self):
        self.timer_num = time(0,0,0)
        self.newtime = time(0,0,0) #no milliseconds
        self.current_date = tk.Label(text=(datetime.date.today()).strftime("%d/%m/%Y"),font=("Arial",20,"bold"))
        self.current_date.grid(row=0,column=0,columnspan=3,sticky="nw",padx=20,pady=20)
        self.TimerButton = tk.Button(self.root, text="Timer",command=self.Timer)
        self.StopwatchButton = tk.Button(self.root, text="Stopwatch",command=self.Stopwatch)
        self.CurrentTimeButton = tk.Button(self.root, text="Current Time",command=self.ShowCurrentTime)
        self.CurrentTimeButton.grid(row=4,column=0)
        self.StopwatchButton.grid(row=4,column=2)
        self.TimerButton.grid(row=4,column=4)

    def check_state(self):
        if self.detected_change == True:
            for widget in self.root.winfo_children():
                widget.destroy()
            self.create_main_widgets()
                
        if self.screen == "CurrentTime":
            currtime = datetime.datetime.now()
            currtime = currtime.strftime('%H:%M:%S')
            if self.detected_change == False:
                self.time_label = tk.Label(self.root,fg="orange",bg="black",text=currtime,font=("Arial",50,"bold"))
                self.time_label.grid(row=2,column=1,columnspan=3,sticky="nsew")
            
        elif self.screen == "Stopwatch":
            if self.detected_change == False:
                self.stopwatch = tk.Label(self.root,fg="orange",bg="black",text=self.newtime)
                self.stopwatch.grid(row=2,column=1,columnspan=3,sticky="nsew")
            else:
                self.stopwatch_start_button = tk.Button(text="START",command=lambda: self.SetStopwatch(False))
                self.stopwatch_start_button.grid(row=2,column=0)
                self.stopwatch_stop_button = tk.Button(text="STOP",command=lambda: self.SetStopwatch(True))
                self.stopwatch_stop_button.grid(row=2,column=4)
            
        elif self.screen == "Timer":
            if self.detected_change == False:
                self.timer_label = tk.Label(self.root,fg="orange",bg="black",text=self.timer_num)
                self.timer_label.grid(row=2,column=1,columnspan=3,sticky="nsew")
            else:
                self.start_timer = tk.Button(text="START",command=lambda:self.SetTimer(False))
                self.stop_timer = tk.Button(text="STOP",command=lambda:self.SetTimer(True))
                self.thirty_sec = tk.Button(text="30s",command=lambda: self.AddTime(30))
                self.one_min = tk.Button(text="1 min",command=lambda: self.AddTime(60))
                self.reset_timer = tk.Button(text="RESET",command=self.ResetTimer)
                self.start_timer.grid(row=2,column=0)
                self.stop_timer.grid(row=2,column=4)
                self.thirty_sec.grid(row=3,column=1)
                self.one_min.grid(row=3,column=2)
                self.reset_timer.grid(row=3,column=3)
            
        self.detected_change = False
        self.root.after(1000,self.check_state)

    def ShowCurrentTime(self):
        self.screen = "CurrentTime"
        self.detected_change = True

    def Stopwatch(self):
        self.screen = "Stopwatch"
        self.detected_change = True
        self.stopped_stopwatch = True
    def StartStopwatch(self):
        if self.stopped_stopwatch == False:
            if self.screen == "Stopwatch":
                seconds = self.newtime.hour * 3600 + self.newtime.minute * 60 + self.newtime.second 
                new_seconds = seconds + 1
                new_hour = (new_seconds // 3600) % 24
                new_minute = (new_seconds % 3600) // 60
                new_second = new_seconds % 60
                self.newtime = time(new_hour, new_minute, new_second)
                self.root.after(1000,self.StartStopwatch)
    def SetStopwatch(self,bool):
        if bool == False:
            self.StartStopwatch()
        self.stopped_stopwatch = bool
        

    def Timer(self):
        self.screen = "Timer"
        self.detected_change = True
        self.stopped_timer = True
    def AddTime(self,add_seconds):
        seconds = self.timer_num.hour * 3600 + self.timer_num.minute * 60 + self.timer_num.second
        new_seconds = seconds + add_seconds
        new_hour = (new_seconds // 3600) % 24
        new_minute = (new_seconds % 3600) // 60
        new_second = new_seconds % 60
        self.timer_num = time(new_hour,new_minute,new_second)
    def StartTimer(self):
        if self.stopped_timer == False:
            total = self.timer_num.hour * 3600 + self.timer_num.minute * 60 + self.timer_num.second
            if total <= 0:
                messagebox.showinfo(message="Timer done!")
            else:
                if self.screen == "Timer":
                    total -= 1 #does not account for milliseconds yet
                    new_hour = (total // 3600) % 24
                    new_minute = (total  % 3600) // 60
                    new_second = total  % 60
                    self.timer_num = time(new_hour,new_minute,new_second)
                    self.root.after(1000,self.StartTimer) #no milliseconds
    def SetTimer(self,bool):
        if bool == False:
            self.StartTimer()
        self.stopped_timer = bool
    def ResetTimer(self):
        self.timer_num = time(0,0,0)
        self.SetTimer(True)
                

if __name__ == "__main__":
    MySmartClock()
