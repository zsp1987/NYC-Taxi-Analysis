#!/usr/bin/env bash
# first delete output files
rm -rf output/q3

# first mapreduce will
$HADOOP_HOME/bin/hadoop  jar $HADOOP_HOME/contrib/streaming/hadoop-streaming-1.0.3.jar \
    -input inputtest/trip_fare_test* \
    -output output/q3/ \
    -mapper q3map.py \
    -reducer q3rd.py
