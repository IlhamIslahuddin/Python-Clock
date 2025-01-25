import tkinter as tk
from datetime import *

class MySmartClock:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("900x500")
        self.root.title("Smart Clock")
        self.root.configure(bg="black")
        self.frame = tk.Frame(self.root)
        self.frame.grid()
        self.TimerButton = tk.Button(self.frame, text="Timer",command=self.Timer)
        self.StopwatchButton = tk.Button(self.frame, text="Stopwatch",command=self.Stopwatch)
        self.CurrentTimeButton = tk.Button(self.frame, text="Current Time",command=self.ShowCurrentTime)
        self.CurrentTimeButton.grid(row=4,column=1)
        self.StopwatchButton.grid(row=4,column=2)
        self.TimerButton.grid(row=4,column=3)
        self.screen = "CurrentTime"
        self.detected_change = False
        self.root.after(0,self.check_state)
        
        self.root.mainloop()

    def check_state(self):
        if self.detected_change == True:
            pass
                
        if self.screen == "CurrentTime":
            currtime = datetime.now()
            currtime = currtime.strftime('%H:%M:%S')
            self.time_label = tk.Label(self.frame,fg="orange",bg="black",text=currtime,font=("Arial",50,"bold"))
            self.time_label.grid(row=2,column=2)
        elif self.screen == "Stopwatch":
            self.stopwatch = tk.Label(self.frame,fg="orange",bg="black",text="00:00:00")
            self.stopwatch.grid(row=3,column=4)
        elif self.screen == "Timer":
            self.timer_label = tk.Label(self.frame,fg="orange",bg="black",text=f"00:00:00")
            self.thirtysec = tk.Button(text="30s")
            self.timer_label.grid(row=3,column=2)
            self.thirtysec.grid(row=4,column=2)
        self.detected_change = False
        self.root.after(1000,self.check_state)

    def ShowCurrentTime(self):
        self.screen = "CurrentTime"
        self.detected_change = True

    def Stopwatch(self):
        self.screen = "Stopwatch"
        self.detected_change = True

    def Timer(self):
        self.screen = "Timer"
        self.detected_change = True

if __name__ == "__main__":
    MySmartClock()
