#!/usr/bin/env sh
rm -rf output/q2
$HADOOP_HOME/bin/hadoop  jar $HADOOP_HOME/contrib/streaming/hadoop-streaming-1.0.3.jar \
	-D mapred.reduce.tasks=2 \
    -input inputtest/trip_fare_test* \
    -output output/q2/ \
    -mapper q2map.py \
    -reducer q2rd.py

