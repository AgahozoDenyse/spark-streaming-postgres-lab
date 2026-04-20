# Real-Time Data Streaming Pipeline

## Overview

This project builds a real-time data pipeline that simulates e-commerce user activity, processes the data using Apache Spark Structured Streaming, and stores the results in a PostgreSQL database.

The system shows how data flows continuously from generation to storage.

---

## Objectives

* Generate real-time event data
* Process streaming data using Spark
* Store processed data in PostgreSQL
* Understand how a data pipeline works

---

## System Components

### 1. Data Generator

A Python script (`data_generator.py`) that creates fake user activity such as product views and purchases.
It continuously generates data and saves it as CSV files.

---

### 2. Data Storage (CSV Files)

Generated data is stored in the folder:

```
data/events/
```

These files act as input for Spark streaming.

---

### 3. Spark Structured Streaming

The Spark application (`spark_streaming_to_postgres.py`) reads the CSV files in real time.

It performs:

* Data cleaning
* Data transformation (e.g., extracting `event_hour`)
* Logging of performance metrics such as processing time and throughput

---

### 4. PostgreSQL Database

Processed data is stored in a PostgreSQL database:

```
events_db
```

Inside the table:

```
user_events
```

This allows querying and analyzing user activity.

---

### 5. Checkpointing

Spark uses the folder:

```
checkpoints/
```

to save progress information.
This helps the system recover if it stops unexpectedly.

---

## Data Flow

Data Generator → CSV Files (`data/events/`) → Spark Structured Streaming → PostgreSQL (`events_db`)
                                           

---

## Technologies Used

* Python
* Apache Spark
* PostgreSQL
* Pandas

---

## Conclusion

This project demonstrates a complete real-time data pipeline, showing how streaming data can be generated, processed, and stored efficiently.

It also highlights important concepts such as data transformation, fault tolerance, and performance monitoring.
