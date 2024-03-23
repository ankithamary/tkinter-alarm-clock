# from tkinter import *
# import datetime
# import time
# from threading import *
# from pygame import mixer

# # create object
# root = Tk()
# root.geometry("500x250")


# def Threading():
#     t1 = Thread(target=alarm)
#     t1.start()


# def alarm():
#     # alarm set to an infinite loop
#     while True:
#         # alarm set
#         set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"
#         time.sleep(1)

#         # get current time
#         current_time = datetime.datetime.now().strftime("%H:%M:%S")
#         print(current_time, set_alarm_time)

#         # condition to check if set time is equal to current time
#         if current_time == set_alarm_time:
#             print("Wake Up now!")
#             # play sound continuously
#             mixer.init()
#             mixer.music.load("sound.wav")
#             mixer.music.play()


# def stop_alarm():
#     mixer.music.stop()


# Label(root, text="Alarm Clock", font=("Helvetica 20 bold"), fg="red").pack(pady=10)
# Label(root, text="Set Time", font=("Helvetica 15 bold")).pack()

# frame = Frame(root)
# frame.pack()

# hour = StringVar(root)
# hours = (
#     "00",
#     "01",
#     "02",
#     "03",
#     "04",
#     "05",
#     "06",
#     "07",
#     "08",
#     "09",
#     "10",
#     "11",
#     "12",
#     "13",
#     "14",
#     "15",
#     "16",
#     "17",
#     "18",
#     "19",
#     "20",
#     "21",
#     "22",
#     "23",
#     "24",
# )
# hour.set(hours[0])

# hrs = OptionMenu(frame, hour, *hours)
# hrs.pack(side=LEFT)

# minute = StringVar(root)
# minutes = (
#     "00",
#     "01",
#     "02",
#     "03",
#     "04",
#     "05",
#     "06",
#     "07",
#     "08",
#     "09",
#     "10",
#     "11",
#     "12",
#     "13",
#     "14",
#     "15",
#     "16",
#     "17",
#     "18",
#     "19",
#     "20",
#     "21",
#     "22",
#     "23",
#     "24",
#     "25",
#     "26",
#     "27",
#     "28",
#     "29",
#     "30",
#     "31",
#     "32",
#     "33",
#     "34",
#     "35",
#     "36",
#     "37",
#     "38",
#     "39",
#     "40",
#     "41",
#     "42",
#     "43",
#     "44",
#     "45",
#     "46",
#     "47",
#     "48",
#     "49",
#     "50",
#     "51",
#     "52",
#     "53",
#     "54",
#     "55",
#     "56",
#     "57",
#     "58",
#     "59",
#     "60",
# )
# minute.set(minutes[0])

# mins = OptionMenu(frame, minute, *minutes)
# mins.pack(side=LEFT)

# second = StringVar(root)
# seconds = (
#     "00",
#     "01",
#     "02",
#     "03",
#     "04",
#     "05",
#     "06",
#     "07",
#     "08",
#     "09",
#     "10",
#     "11",
#     "12",
#     "13",
#     "14",
#     "15",
#     "16",
#     "17",
#     "18",
#     "19",
#     "20",
#     "21",
#     "22",
#     "23",
#     "24",
#     "25",
#     "26",
#     "27",
#     "28",
#     "29",
#     "30",
#     "31",
#     "32",
#     "33",
#     "34",
#     "35",
#     "36",
#     "37",
#     "38",
#     "39",
#     "40",
#     "41",
#     "42",
#     "43",
#     "44",
#     "45",
#     "46",
#     "47",
#     "48",
#     "49",
#     "50",
#     "51",
#     "52",
#     "53",
#     "54",
#     "55",
#     "56",
#     "57",
#     "58",
#     "59",
#     "60",
# )
# second.set(seconds[0])

# secs = OptionMenu(frame, second, *seconds)
# secs.pack(side=LEFT)

# Button(root, text="Set Alarm", font=("Helvetica 15"), command=Threading).pack(pady=20)

# button = Button(root, text="Stop Alarm", bg="red", fg="white", command=stop_alarm).pack(
#     pady=30
# )

# root.mainloop()
from tkinter import *
import datetime
import time
from threading import *
from pygame import mixer

# Create object
root = Tk()
root.geometry("500x300")
root.title("Alarm Clock")

# Global variable to control the alarm
stop_alarm_flag = False

def Threading():
    t1 = Thread(target=alarm)
    t1.start()

def alarm():
    global stop_alarm_flag
    
    # alarm set to an infinite loop
    while True:
        # Check if the stop alarm flag is set
        if stop_alarm_flag:
            break
        
        # alarm set
        set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"
        time.sleep(1)

        # get current time
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time, set_alarm_time)

        # condition to check if set time is equal to current time
        if current_time == set_alarm_time:
            print("Wake Up now!")
            # play sound continuously
            mixer.init()
            mixer.music.load("sound.wav")
            mixer.music.play()

def stop_alarm():
    global stop_alarm_flag
    # Set the stop alarm flag to True
    stop_alarm_flag = True

# Labels and Widgets
Label(root, text="Alarm Clock", font=("Helvetica 20 bold")).pack(pady=10)

frame = Frame(root)
frame.pack()

hour = StringVar(root)
hours = ["{:02d}".format(i) for i in range(24)]
hour.set(hours[0])

hrs = OptionMenu(frame, hour, *hours)
hrs.pack(side=LEFT)

minute = StringVar(root)
minutes = ["{:02d}".format(i) for i in range(60)]
minute.set(minutes[0])

mins = OptionMenu(frame, minute, *minutes)
mins.pack(side=LEFT)

second = StringVar(root)
seconds = ["{:02d}".format(i) for i in range(60)]
second.set(seconds[0])

secs = OptionMenu(frame, second, *seconds)
secs.pack(side=LEFT)

# Button to set alarm
Button(root, text="Set Alarm", font=("Helvetica 15"), command=Threading).pack(pady=20)

# Button to stop alarm
Button(root, text="Stop Alarm", bg="red", fg="white", command=stop_alarm).pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
