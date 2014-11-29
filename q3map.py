#!/usr/bin/env python

import sys, datetime

def parseInput():
    for line in sys.stdin:
        line = line.strip()
        values = line.split(',')
        if len(values)>1 and values[0]!='medallion':
            yield values

def mapper():
    for value in parseInput():
        medallion = value[0]
        drv_lcn  = value[1]
        pic_tm = value[5]
        dp_tm = value[6]
        pic_dt = datetime.datetime.strptime(pic_tm, '%Y-%m-%d %H:%M:%S')
        pic_date = pic_dt.strptime("%Y-%m-%d")
        print "%s\t%s\t%s\t%s\t%s"