#!/usr/bin/env sh
rm -rf output/q2
$HADOOP_HOME/bin/hadoop  jar $HADOOP_HOME/contrib/streaming/hadoop-streaming-1.0.3.jar \
    -input input/trip_fare_1.csv \
    -output output/q2/ \
    -mapper q2map.py \
    -reducer q2rd.py

