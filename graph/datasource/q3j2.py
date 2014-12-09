import sys

for line in sys.stdin:
	date, avg1, sum1 = line.split('\t')
	print '[%s, %s],' % (avg1, sum1.strip())