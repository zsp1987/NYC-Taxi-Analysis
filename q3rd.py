#!/usr/bin/env python
import itertools, operator, sys, datetime

def parseInput():
    for line in sys.stdin:
        yield line.strip('\n').split('\t')

def reducer():
    for key, values in itertools.groupby(parseInput(), operator.itemgetter(0,1,2)):
        minutes = 0
        last_drp_time = None
        for value in values:
            pick_time = datetime.datetime.strptime(value[3], "%Y-%m-%d %H:%M:%S")
            drp_time = datetime.datetime.strptime(value[4], "%Y-%m-%d %H:%M:%S")
            if last_drp_time:
                minutes += (pick_time-last_drp_time).seconds/60.0
            last_drp_time=drp_time
        print '%s\t%s' % (key, minutes)

if __name__=='__main__':
    reducer()