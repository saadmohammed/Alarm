import time
from datetime import datetime, date
from playsound import playsound


#showing current time
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)
alarm_time = input("Enter time in HH:MM:SS")
objtime = datetime.strptime(alarm_time,  '%H:%M:%S')
print('Alarm time', objtime.time())
sub = datetime.combine(date.today(), objtime.time()) - datetime.combine(date.today(), datetime.time(datetime.now()))
sec = sub.total_seconds()
time.sleep(round(sec))
print("Wake Up")
for i in range(20):
    playsound('C:\\Users\\ELCOT\\PycharmProjects\\Alarm\\audio.mp3')
