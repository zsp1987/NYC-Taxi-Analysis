#!/usr/bin/env bash
# first delete output files
rm -rf output/q3

# test code
cat inputtest/trip_data_test_1 | python q3map.py| sort

# first mapreduce will
$HADOOP_HOME/bin/hadoop  jar $HADOOP_HOME/contrib/streaming/hadoop-streaming-1.0.3.jar \
    -input inputtest/trip_fare_test* \
    -output output/q3/ \
    -mapper q3map.py \
    -reducer q3rd.py
