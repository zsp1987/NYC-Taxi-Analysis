#!/usr/bin/env python

import sys

def parseInput():
    try:
        for line in sys.stdin:
            line = line.strip()
            values = line.split(',')
            if len(values)>1 and values[0]!='medallion':
                yield values
    except Exception  as e:
        pass


def mapper():
    try:
        for value in parseInput():
            total_amount = float(value[10])
            pickup_time = value[3]
            month = pickup_time.split('-')[1]
            print "%s\t%s" % (month, total_amount)
    except Exception  as e:
        pass

if __name__=='__main__':
    mapper()