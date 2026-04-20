"""
Spark Structured Streaming with logging and performance tracking
"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, hour, to_timestamp
import logging
import time
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, DoubleType

# Logging setup
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

spark = SparkSession.builder \
    .appName("StreamingToPostgres") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

INPUT_DIR = "data/events"
CHECKPOINT_DIR = "checkpoints"

JDBC_URL = "jdbc:postgresql://localhost:5432/events_db"
PROPS = {
    "user": "postgres",
    "password": "securepassword",
    "driver": "org.postgresql.Driver"
}

TABLE = "user_events"


schema = StructType([
    StructField("user_id", IntegerType()),
    StructField("event_type", StringType()),
    StructField("product_id", IntegerType()),
    StructField("product_name", StringType()),
    StructField("price", DoubleType()),
    StructField("timestamp", StringType())
])

df = spark.readStream.schema(schema).csv(INPUT_DIR)

clean_df = df \
    .withColumn("event_time", to_timestamp(col("timestamp"))) \
    .drop("timestamp") \
    .filter(col("price") > 0) \
    .filter(col("user_id").isNotNull()) \
    .withColumn("event_hour", hour(col("event_time")))

def write_batch(batch_df, batch_id):
    """
    This function processes and saves each batch of streaming data.

    It is called automatically by Spark for every batch of data.

    The function:
    - Counts the number of rows in the batch
    - Writes the batch data into the PostgreSQL database
    - Measures how long the batch takes to process
    - Logs useful information like number of rows, time taken, and speed (throughput)

    If an error happens, it logs the error message.

"""
    start_time = time.time()

    try:
        count = batch_df.count()

        batch_df.write.jdbc(
            url=JDBC_URL,
            table=TABLE,
            mode="append",
            properties=PROPS
        )

        duration = time.time() - start_time

        logger.info(
            f"Batch {batch_id} | Rows: {count} | "
            f"Time: {duration:.2f}s | "
            f"Throughput: {count/duration:.2f} rows/sec"
        )

    except Exception as e:
        logger.error(f"Error in batch {batch_id}: {e}")

query = clean_df.writeStream \
    .foreachBatch(write_batch) \
    .option("checkpointLocation", CHECKPOINT_DIR) \
    .start()

logger.info("Streaming query started...")

query.awaitTermination()
