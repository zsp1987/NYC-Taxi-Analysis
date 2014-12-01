__author__ = 'haochen'

f = open('BigEvent','r')
line = f.readline().strip().split()
print line
EventMonth = line[1]
print EventMonth
EventDay = line[1].strip().split('-')
print EventDay
if '7' in EventDay:
    print True;