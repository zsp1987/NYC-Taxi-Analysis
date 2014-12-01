rm -rf output/EveryDayRevenue
$HADOOP_HOME/bin/hadoop  jar $HADOOP_HOME/contrib/streaming/hadoop-streaming-1.0.3.jar \
    -input inputtest/trip_fare_test* \
    -output output/EveryDayRevenue/ \
    -mapper EveryDayRevenue.py \
    -reducer EveryDayRevenueRe.py


