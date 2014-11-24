#!/usr/bin/env sh
$HADOOP_HOME/bin/hadoop  jar $HADOOP_HOME/contrib/streaming/hadoop-streaming-1.0.3.jar \
	-D mapred.reduce.tasks=2 \
    -input inputtest \
    -output output \
    -mapper question2mapper.py \
    -reducer question2reducer.py
