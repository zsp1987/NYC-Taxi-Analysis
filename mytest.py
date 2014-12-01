__author__ = 'haochen'


f1 = open('BigEvent','r')
Event = f1.readline().strip().split()
EventMonth = Event[0]
EventDay = Event[1].strip().split('-')
f = open('output/EveryDayRevenue/part-00000','r')
line = f.readlines()
for day in line:
    day1 = day.strip().split('\t')
    day2 = day1[0].strip().split('-')
    month = day2[1]
    dayRevenue = day2[2]
    if EventMonth == month:
        if dayRevenue in EventDay:
            print day

