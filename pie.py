import matplotlib.pyplot as plt
 
# Data to plot
labels = 'Python', 'C++', 'Ruby', 'Java'
sizes = [215, 130, 245, 210]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.1, 0, 0, 0)  # explode 1st slice
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')
plt.show()

#############

from icalendar import Calendar
from datetime import timedelta
from itertools import groupby
from operator import itemgetter


def calculate_time(event):
    start = event['DTSTART'].dt
    end = event['DTEND'].dt
    return end - start


def lecturize(event):
    summary = str(event['SUMMARY'])
    for lecture in lectures:
        if lecture in summary:
            return lecture


def time_per_lecture(events):
    sorted_events = sorted(events, key=itemgetter(0))
    for key, group in groupby(sorted_events, itemgetter(0)):
        yield (key, sum(map(itemgetter(1), group), timedelta()))

lectures = ['An1I', 'Math1I', 'Bsys1', 'CN1', 'EnglHTw', 'Prog1', 'ICTh']
file = open('examtime_export.ics', 'rb')
cal = Calendar.from_ical(file.read())
events = [(lecturize(e), calculate_time(e)) for e in cal.walk('vevent')]
events = [e for e in events if e[0] != None]

used_time = dict(time_per_lecture(events))
total_time = sum(used_time.values(), timedelta())

for lecture, time in used_time.items():
    print('{}\t{}h'.format(lecture, time.total_seconds() / 3600))

print('=============')
print('TOTAL\t{}h'.format(total_time.total_seconds() / 3600))