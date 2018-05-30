"""
Alarm clock
"""
import time

while True:
	try:
		hour = int(input("Enter the alarm time(hour):"))
		minute = int(input("Enter the alarm time(minute):"))
		second = int(input("Enter the alarm time(second):"))

		break
	except ValueError:
		print("Please enter a number representing time in seconds:")

alarmtime = time.time() + (hour*60*60) + (minute*60) + second

while alarmtime >= time.time():
	time.sleep(0.01)


print ("Alarm!\x07")