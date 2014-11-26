#!/usr/bin/env sh
rm -rf output/q1
$HADOOP_HOME/bin/hadoop  jar $HADOOP_HOME/contrib/streaming/hadoop-streaming-1.0.3.jar \
	-D mapred.reduce.tasks=2 \
    -input trip_date_test \n
    -output output/q1 \
    -mapper q1map.py \
    -reducer q2rd.py \
