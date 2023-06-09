import pyspark.sql.types as T

PRODUCE_TOPIC_RIDES_CSV = CONSUME_TOPIC_RIDES_CSV = 'rides_csv'
BOOTSTRAP_SERVERS = 'localhost:9092'

TOPIC_WINDOWED_VENDOR_ID_COUNT = 'vendor_counts_windowed'

RIDE_SCHEMA1 = T.StructType(
    [T.StructField("vendor_id", T.IntegerType()),
     T.StructField('tpep_pickup_datetime', T.StringType()),
     T.StructField('tpep_dropoff_datetime', T.StringType()),
     T.StructField("passenger_count", T.IntegerType()),
     T.StructField("trip_distance", T.FloatType()),
     T.StructField("rate_code_id", T.IntegerType()),
     T.StructField("store_and_fwd_flag", T.StringType()),
     T.StructField("pu_location_id", T.IntegerType()),
     T.StructField("do_location_id", T.IntegerType()),
     T.StructField("payment_type", T.StringType()),
     T.StructField("fare_amount", T.FloatType()),
     T.StructField("extra", T.FloatType()),
     T.StructField("mta_tax", T.FloatType()),
     T.StructField("tip_amount", T.FloatType()),
     T.StructField("tolls_amount", T.FloatType()),
     T.StructField("improvement_surcharge", T.FloatType()),
     T.StructField("total_amount", T.FloatType()),
     T.StructField("congestion_surcharge", T.FloatType()),
     ])

RIDE_SCHEMA = T.StructType(
 [T.StructField("vendor_id", T.IntegerType()),
  T.StructField('tpep_pickup_datetime', T.TimestampType()),
  T.StructField('tpep_dropoff_datetime', T.TimestampType()),
  T.StructField("passenger_count", T.IntegerType()),
  T.StructField("trip_distance", T.FloatType()),
  T.StructField("payment_type", T.IntegerType()),
  T.StructField("total_amount", T.FloatType()),
  ])