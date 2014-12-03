#!/usr/bin/env python
import itertools, operator, sys, datetime

def parseInput():
    for line in sys.stdin:
        if len(line)>0:
            line = line.strip()


def reducer():
    current_key = None
    current_list = []
    for line in parseInput():
        key, pic_tm, drp_tm = line.split('\t')
        try:
            pic_tm = datetime.datetime.strptime(pic_tm, "%Y-%m-%d %H:%M:%S")
            drp_tm = datetime.datetime.strptime(drp_tm, "%Y-%m-%d %H:%M:%S")
        except E:
            continue
        if current_key == key:
            current_key.append((pic_tm, drp_tm))   
        else:
            if current_key and current_list:
                current_list.sort()
                last_drp_tm = None
                minutes = 0
                for pic_tm,drp_tm in current_list:
                    if last_drp_tm:
                        minutes += (pic_tm - last_drp_tm).seconds/60.0
                    last_drp_tm = drp_tm
                print '%s\t%s' % (current_key[-10], minutes)
            
            current_key = key
            current_list = []
    if current_key == key:
        current_list.sort()
        last_drp_tm = None
        minutes = 0
        for pic_tm,drp_tm in current_list:
            if last_drp_tm:
                minutes += (pic_tm - last_drp_tm).seconds/60.0
            last_drp_tm = drp_tm
        print '%s\t%s' % (current_key[-10], minutes)

if __name__=='__main__':
    reducer()








if __name__=='__main__':
    reducer()