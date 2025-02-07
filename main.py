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
        self.root.grid_rowconfigure(0,weight=1)
        self.root.grid_columnconfigure(0,weight=1)
        self.main_frame = tk.Frame(self.root)
        self.main_frame.configure(bg="black")
        self.main_frame.grid(row=0,column=0,sticky="nsew")
        self.main_frame.columnconfigure(0,weight=1)
        self.main_frame.columnconfigure(1,weight=1)
        self.main_frame.columnconfigure(2,weight=1)
        self.main_frame.columnconfigure(3,weight=1)
        self.main_frame.columnconfigure(4,weight=1)
        self.main_frame.rowconfigure(0,weight=1)
        self.main_frame.rowconfigure(1,weight=1)
        self.main_frame.rowconfigure(2,weight=1)
        self.main_frame.rowconfigure(3,weight=1)
        self.main_frame.rowconfigure(4,weight=1)
        self.timer_frame = tk.Frame(self.main_frame, bg="black")
        # self.timer_frame.grid(row=0,column=0,sticky="nsew")
        self.timer_frame.columnconfigure(0,weight=1)
        self.timer_frame.columnconfigure(1,weight=1)
        self.timer_frame.columnconfigure(2,weight=1)
        self.timer_frame.columnconfigure(3,weight=1)
        self.timer_frame.columnconfigure(4,weight=1)
        self.timer_frame.rowconfigure(0,weight=1)
        self.timer_frame.rowconfigure(1,weight=1)
        self.timer_frame.rowconfigure(2,weight=1)
        self.timer_frame.rowconfigure(3,weight=1)
        self.timer_frame.rowconfigure(4,weight=1)
        self.stopwatch_frame = tk.Frame(self.main_frame, bg="black")
        # self.stopwatch_frame.grid(row=0,column=0,sticky="nsew")
        self.stopwatch_frame.columnconfigure(0,weight=1)
        self.stopwatch_frame.columnconfigure(1,weight=1)
        self.stopwatch_frame.columnconfigure(2,weight=1)
        self.stopwatch_frame.columnconfigure(3,weight=1)
        self.stopwatch_frame.columnconfigure(4,weight=1)
        self.stopwatch_frame.rowconfigure(0,weight=1)
        self.stopwatch_frame.rowconfigure(1,weight=1)
        self.stopwatch_frame.rowconfigure(2,weight=1)
        self.stopwatch_frame.rowconfigure(3,weight=1)
        self.stopwatch_frame.rowconfigure(4,weight=1)
        self.currenttime_frame = tk.Frame(self.main_frame, bg="black")
        self.currenttime_frame.grid(row=0,column=0,sticky="nsew")
        self.currenttime_frame.columnconfigure(0,weight=1)
        self.currenttime_frame.columnconfigure(1,weight=1)
        self.currenttime_frame.columnconfigure(2,weight=1)
        self.currenttime_frame.columnconfigure(3,weight=1)
        self.currenttime_frame.columnconfigure(4,weight=1)
        self.currenttime_frame.rowconfigure(0,weight=1)
        self.currenttime_frame.rowconfigure(1,weight=1)
        self.currenttime_frame.rowconfigure(2,weight=1)
        self.currenttime_frame.rowconfigure(3,weight=1)
        self.currenttime_frame.rowconfigure(4,weight=1)
        
        self.timer_num = time(0,0,0)
        self.newtime = time(0,0,0)
        self.milliseconds = 0
        self.current_date = tk.Label(self.main_frame,text=(datetime.date.today()).strftime("%d/%m/%Y"),font=("Arial",20,"bold"))
        self.current_date.grid(row=0,column=0,columnspan=3,sticky="nw",padx=20,pady=20)
        self.TimerButton = tk.Button(self.main_frame, text="Timer",command=self.Timer)
        self.StopwatchButton = tk.Button(self.main_frame, text="Stopwatch",command=self.Stopwatch)
        self.CurrentTimeButton = tk.Button(self.main_frame, text="Current Time",command=self.CurrentTime)
        self.CurrentTimeButton.grid(row=4,column=0)
        self.StopwatchButton.grid(row=4,column=2)
        self.TimerButton.grid(row=4,column=4)
        
        self.root.mainloop()

    
    def CreateTimerScreen(self):
        self.timer_frame.place(relx=0.5,rely=0.5,anchor="center",relheight=0.7,relwidth=0.7)
        self.timer_frame.lift()
        self.timer_label = tk.Label(self.timer_frame,fg="orange",bg="black",text=f"{self.timer_num}:{self.milliseconds:03}",font=("Arial",50,"bold"))
        self.timer_label.grid(row=1,column=1,columnspan=3,sticky="nsew")
        self.start_timer = tk.Button(self.timer_frame,text="START",command=lambda:self.SetTimer(False))
        self.stop_timer = tk.Button(self.timer_frame,text="STOP",command=lambda:self.SetTimer(True))
        self.thirty_sec = tk.Button(self.timer_frame,text="30s",command=lambda: self.AddTime(30))
        self.one_min = tk.Button(self.timer_frame,text="1 min",command=lambda: self.AddTime(60))
        self.one_hour = tk.Button(self.timer_frame,text="1 hour",command=lambda: self.AddTime(3600))
        self.reset_timer = tk.Button(self.timer_frame,text="RESET",command=self.ResetTimer)
        self.start_timer.grid(row=2,column=0)
        self.stop_timer.grid(row=2,column=4)
        self.thirty_sec.grid(row=3,column=1)
        self.one_min.grid(row=3,column=2)
        self.one_hour.grid(row=3,column=3)
        self.reset_timer.grid(row=3,column=4)
    def CreateStopwatchScreen(self):
        self.stopwatch_frame.place(relx=0.5,rely=0.5,anchor="center",relheight=0.7,relwidth=0.7)
        self.stopwatch_frame.lift()
        self.stopwatch = tk.Label(self.stopwatch_frame,fg="orange",bg="black",text=f"{self.newtime}:{self.milliseconds:03}",font=("Arial",50,"bold"))
        self.stopwatch.grid(row=2,column=1,columnspan=3,sticky="nsew")
        self.stopwatch_start_button = tk.Button(self.stopwatch_frame,text="START",command=lambda: self.SetStopwatch(False))
        self.stopwatch_start_button.grid(row=2,column=0)
        self.stopwatch_stop_button = tk.Button(self.stopwatch_frame,text="STOP",command=lambda: self.SetStopwatch(True))
        self.stopwatch_stop_button.grid(row=2,column=4)
        self.stopwatch_reset_button = tk.Button(self.stopwatch_frame,text="RESET",command=self.ResetStopwatch)
        self.stopwatch_reset_button.grid(row=3,column=4)
    def CreateCurrentTimeScreen(self):
        if self.screen == "CurrentTime":
            self.currenttime_frame.place(relx=0.5,rely=0.5,anchor="center",relheight=0.7,relwidth=0.7)
            self.currenttime_frame.lift()
            currtime = datetime.datetime.now()
            currtime = currtime.strftime('%H:%M:%S')
            self.time_label = tk.Label(self.currenttime_frame,fg="orange",bg="black",text=currtime,font=("Arial",50,"bold"))
            self.time_label.grid(row=2,column=1,columnspan=3,sticky="nsew")
            self.root.after(1000,self.CreateCurrentTimeScreen)
                
    def CurrentTime(self):
        self.timer_frame.place_forget()
        self.stopwatch_frame.place_forget()
        self.currenttime_frame.place_forget()
        self.screen = "CurrentTime"
        self.CreateCurrentTimeScreen()

    def Stopwatch(self):
        self.timer_frame.place_forget()
        self.stopwatch_frame.place_forget()
        self.currenttime_frame.place_forget()
        self.milliseconds = 0
        self.screen = "Stopwatch"
        self.stopped_stopwatch = True
        self.CreateStopwatchScreen()
    def StartStopwatch(self):
        if self.stopped_stopwatch == False:
            if self.screen == "Stopwatch":
                self.milliseconds += 1
                if self.milliseconds >= 1000:
                    self.milliseconds = 0
                    seconds = self.newtime.hour * 3600 + self.newtime.minute * 60 + self.newtime.second + 1
                else:
                    seconds = self.newtime.hour * 3600 + self.newtime.minute * 60 + self.newtime.second
                new_hour = (seconds // 3600) % 24
                new_minute = (seconds % 3600) // 60
                new_second = seconds % 60
                self.newtime = time(new_hour, new_minute, new_second)
                self.stopwatch.configure(text=f"{self.newtime}:{self.milliseconds:03}")
                self.root.after(1,self.StartStopwatch)
    def SetStopwatch(self,bool):
        if self.stopped_stopwatch != bool:
            self.stopped_stopwatch = bool
            if bool == False:
                self.StartStopwatch()
    def ResetStopwatch(self):
        self.newtime = time(0,0,0)
        self.stopwatch.configure(text=self.newtime)
        self.SetStopwatch(True)
        
    def Timer(self):
        self.timer_frame.grid_forget()
        self.stopwatch_frame.grid_forget()
        self.currenttime_frame.grid_forget()
        self.milliseconds = 0
        self.screen = "Timer"
        self.stopped_timer = True
        self.CreateTimerScreen()
    def AddTime(self,add_seconds):
        seconds = self.timer_num.hour * 3600 + self.timer_num.minute * 60 + self.timer_num.second + add_seconds
        new_hour = (seconds // 3600) % 24
        new_minute = (seconds % 3600) // 60
        new_second = seconds % 60
        self.timer_num = time(new_hour,new_minute,new_second)
        self.timer_label.configure(text=f"{self.timer_num}:{self.milliseconds:03}")
    def StartTimer(self):
        if self.stopped_timer == False:
            self.milliseconds -= 1
            if self.milliseconds < 0:
                self.milliseconds = 999
                total = self.timer_num.hour * 3600 + self.timer_num.minute * 60 + self.timer_num.second - 1
            else:
                total = self.timer_num.hour * 3600 + self.timer_num.minute * 60 + self.timer_num.second
            if total <= 0:
                self.ResetTimer()
                messagebox.showinfo(message="Timer done!")
            else:
                if self.screen == "Timer":
                    new_hour = (total // 3600) % 24
                    new_minute = (total  % 3600) // 60
                    new_second = total  % 60
                    self.timer_num = time(new_hour,new_minute,new_second)
                    self.timer_label.configure(text=f"{self.timer_num}:{self.milliseconds:03}")
                    self.root.after(1,self.StartTimer)
    def SetTimer(self,bool):
        self.stopped_timer = bool
        if bool == False:
            self.StartTimer()
    def ResetTimer(self):
        self.timer_num = time(0,0,0)
        self.milliseconds = 0
        self.timer_label.configure(text=f"{self.timer_num}:{self.milliseconds:03}")
        self.SetTimer(True)
                
if __name__ == "__main__":
    MySmartClock()
