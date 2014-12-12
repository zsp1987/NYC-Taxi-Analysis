FARE_RAW = LOAD 'trip_fare_{[1-9],10,11,12}.csv' USING PigStorage(',') AS (medallion:chararray, hack_license:chararray, vendor_id:chararray, pickup_datetime:chararray, payment_type:chararray, fare_amount:double, surcharge:double, mta_tax:double, tip_amount:double, tolls_amount:double, total_amount:double);

FARE = FILTER FARE_RAW BY medallion != 'medallion';

FOREACH FARE BY (total_amount < 0 or )