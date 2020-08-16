
# Create a spark session to use the  DataSOurce api in order to process stream data using the SQL Engine
from pyspark.sql import SparkSession

import pyspark.sql.functions as psf
from pyspark.sql import Window

spark = SparkSession.builder.appName("AggApplication").getOrCreate()

# Define a check point so that the Compiler(The JVM compiler) refer to that point whenever an erreurs accures
spark.conf.set("spark.sql.streaming.checkpointLocation","./Checkpoints/checkpoint")


dfstream=spark.readStream.format("kafka").option("kafka.bootstrap.servers","localhost:9092").option("subscribe",'dataaggregation'.option("maxOffsetsPerTrigger",2000).load())
w = Window.orderBy('datetime')
windowedCountsDF =   eventsDF.groupBy( "id", window("eventTime", "5 minutes")).count()