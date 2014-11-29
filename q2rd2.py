#!/usr/bin/env python
import itertools, operator, sys

def parseInput():
    for line in sys.stdin:
        yield line.strip('\n').split('\t')

def reducer():
    for key, values in itertools.groupby(parseInput(), operator.itemgetter(0)):
        print '%s\t%s' % (key, values)

if __name__=='__main__':
    reducer()
