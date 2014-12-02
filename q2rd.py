#!/usr/bin/env python
import itertools, operator, sys

def parseInput():
    try:
        for line in sys.stdin:
            yield line.strip('\n').split('\t')
    except Exception as e:
        pass

def reducer():
    try:
        for key, values in itertools.groupby(parseInput(), operator.itemgetter(0)):
            count = sum(map(float, zip(*values)[1]))
            print '%s\t%s' % (key, count)
    except Exception as e:
        pass

if __name__=='__main__':
    reducer()