import tkinter as tk
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
        self.root.rowconfigure(0,weight=1)
        self.root.rowconfigure(1,weight=1)
        self.root.rowconfigure(2,weight=1)
        # self.current_date = tk.Label(text=(datetime.date.today()).strftime("%d/%m/%Y"))
        # self.current_date.grid(row=0,column=0,sticky="nw",padx=10,pady=10)
        # self.TimerButton = tk.Button(self.root, text="Timer",command=self.Timer)
        # self.StopwatchButton = tk.Button(self.root, text="Stopwatch",command=self.Stopwatch)
        # self.CurrentTimeButton = tk.Button(self.root, text="Current Time",command=self.ShowCurrentTime)
        # self.CurrentTimeButton.grid(row=2,column=0)
        # self.StopwatchButton.grid(row=2,column=1)
        # self.TimerButton.grid(row=2,column=2)
        self.create_main_widgets()
        self.screen = "CurrentTime"
        self.detected_change = False
        self.root.after(0,self.check_state)
        
        self.root.mainloop()
        
    def create_main_widgets(self):
        self.current_date = tk.Label(text=(datetime.date.today()).strftime("%d/%m/%Y"),font=("Arial",20,"bold"))
        self.current_date.grid(row=0,column=0,sticky="nw",padx=20,pady=20)
        self.TimerButton = tk.Button(self.root, text="Timer",command=self.Timer)
        self.StopwatchButton = tk.Button(self.root, text="Stopwatch",command=self.Stopwatch)
        self.CurrentTimeButton = tk.Button(self.root, text="Current Time",command=self.ShowCurrentTime)
        self.CurrentTimeButton.grid(row=2,column=0)
        self.StopwatchButton.grid(row=2,column=1)
        self.TimerButton.grid(row=2,column=2)

    def check_state(self):
        if self.detected_change == True:
            for widget in self.root.winfo_children():
                widget.destroy()
            self.create_main_widgets()
                
        if self.screen == "CurrentTime":
            currtime = datetime.datetime.now()
            currtime = currtime.strftime('%H:%M:%S')
            self.time_label = tk.Label(self.root,fg="orange",bg="black",text=currtime,font=("Arial",50,"bold"))
            self.time_label.grid(row=1,column=1,sticky="nsew")
            
        elif self.screen == "Stopwatch":
            self.StartStopwatch()
            self.stopwatch = tk.Label(self.root,fg="orange",bg="black",text=self.newtime)
            self.stopwatch.grid(row=1,column=1)
            # self.start = tk.Button(self.root,text="START",command=self.StartStopwatch)
            # self.start.grid(row=1,column=2)
            
        elif self.screen == "Timer":
            self.timer_label = tk.Label(self.root,fg="orange",bg="black",text=f"00:00:00")
            self.thirtysec = tk.Button(text="30s")
            self.timer_label.grid(row=1,column=1)
            self.thirtysec.grid(row=2,column=1)
            
        self.detected_change = False
        self.root.after(1000,self.check_state)

    def ShowCurrentTime(self):
        self.screen = "CurrentTime"
        self.detected_change = True

    def Stopwatch(self):
        self.screen = "Stopwatch"
        self.detected_change = True
        self.newtime = time(0,0,0)
    def StartStopwatch(self):
        seconds = self.newtime.hour * 3600 + self.newtime.minute * 60 + self.newtime.second
        new_seconds = seconds + 1
        new_hour = (new_seconds // 3600) % 24
        new_minute = (new_seconds % 3600) // 60
        new_second = new_seconds % 60
        self.new_time = time(new_hour, new_minute, new_second)
        print (f"here {self.new_time}")
        

    def Timer(self):
        self.screen = "Timer"
        self.detected_change = True

if __name__ == "__main__":
    MySmartClock()
