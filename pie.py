import matplotlib.pyplot as plt
from icalendar import Calendar
from datetime import timedelta
import os

# I am assuming we have exported each calendar as its own ics file 

def calculate_time(event):
    start = event['DTSTART'].dt
    end = event['DTEND'].dt
    return end - start

labels = []
totals = []
path = 'cals/'

for filename in os.listdir(path):
	file = open(path+filename, 'rb')
	cal = Calendar.from_ical(file.read())

	#this is a list of the time deltas 
	times = [calculate_time(e) for e in cal.walk('vevent')]
	# events = [e for e in events if e[0] != None]

	total_time = 0 
	for time in times:
		total_time += time.seconds/3600

	totals.append(total_time)
	name = os.path.splitext(os.path.basename(filename))[0].lower()
	labels.append(name)
	print name + ': ' +  str(total_time)

	# get earliest element of any calendar 
	# if curr_first_time < earliest:
	# 		earliest = curr_first_time 

# total_duration = latest - earliest

### PLOTTING
 
plt.pie(totals, labels=labels, autopct='%1.1f%%') 
plt.axis('equal')
plt.show()

