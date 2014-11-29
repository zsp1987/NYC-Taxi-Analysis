#!/usr/bin/env sh
rm -rf output/q1
$HADOOP_HOME/bin/hadoop  jar $HADOOP_HOME/contrib/streaming/hadoop-streaming-1.0.3.jar \
	-D mapred.reduce.tasks=2 \
    -input inputtest/trip_date_test \
    -output output/q1 \
    -mapper q1map.py \
    -reducer q1rd.py \
