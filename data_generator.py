"""
data_generator.py

Simulates high-throughput real-time e-commerce events.

This script continuously generates CSV files containing user activity
(e.g., product views and purchases) and writes them to a directory
monitored by Spark Structured Streaming.

Key Features:
- Generates large-scale event batches (1000+ events)
- Uses sequential timestamps to simulate real-time data
- Implements atomic file writes to avoid partial reads
- Includes logging and error handling for robustness
"""

import os
import time
import uuid
import pandas as pd
import random
import logging
from datetime import datetime, timedelta, timezone

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

logger = logging.getLogger(__name__)

OUTPUT_DIR = "data/events"
BATCH_SIZE = 1000
SLEEP_INTERVAL = 1

os.makedirs(OUTPUT_DIR, exist_ok=True)

PRODUCTS = [
    (1, "Laptop", 1200.50),
    (2, "Phone", 800.00),
    (3, "Headphones", 150.75),
    (4, "Monitor", 300.20),
    (5, "Keyboard", 75.00)
]

def generate_batch(start_time):
    """
    This function creates a batch of fake e-commerce events.

    It generates many records (1000 events) where each record represents
    a user action such as viewing or purchasing a product.

    Each event includes:
    - user ID
    - event type (view or purchase)
    - product information
    - timestamp

    The timestamps are slightly different for each event to simulate real-time data.
    """
    events = []

    for i in range(BATCH_SIZE):
        product = random.choice(PRODUCTS)
        event_time = start_time + timedelta(milliseconds=i)

        events.append({
            "user_id": random.randint(1, 1000),
            "event_type": random.choices(["view", "purchase"],weights=[0.8,0.2])[0],
            "product_id": product[0],
            "product_name": product[1],
            "price": product[2],
            "timestamp": event_time.strftime("%Y-%m-%d %H:%M:%S")
        })

    return events


def save_atomic(df):
    """
     This function saves the generated data into a CSV file safely.

    It first writes the data to a temporary file, then renames it
    to the final file name.

    This prevents Spark from reading incomplete files while they are still being written.  """

    tmp_file = f"{OUTPUT_DIR}/tmp_{uuid.uuid4().hex}.csv"
    final_file = tmp_file.replace("tmp_", "events_")

    df.to_csv(tmp_file, index=False)
    os.rename(tmp_file, final_file)

    logger.info(f"Saved file: {final_file}")


def main():
    """
    This is the main function that runs the data generator continuously.

    It:
    - Starts the data generation process
    - Calls generate_batch() to create data
    - Converts the data into a DataFrame
    - Calls save_atomic() to save the data
    - Waits for a short time before generating the next batch

    This loop runs forever until the user stops it.
    """
    logger.info("Starting data generator...")

    current_time = datetime.now(timezone.utc)

    while True:
        try:
            batch = generate_batch(current_time)
            df = pd.DataFrame(batch)

            save_atomic(df)

            current_time += timedelta(seconds=1)
            time.sleep(SLEEP_INTERVAL)

        except Exception as e:
            logger.error(f"Generator error: {e}")


#This ensures that the main() function runs only when the script is executed directly.
#It starts the data generator program.

if __name__ == "__main__":
    main()
