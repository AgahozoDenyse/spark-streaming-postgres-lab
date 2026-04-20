# Real-Time Data Streaming Pipeline Lab - User Guide

---

## Overview

This guide provides step-by-step instructions to run the real-time data pipeline.

The system generates data, processes it using Apache Spark, and stores it in PostgreSQL.

---

## Project Structure

```
spark-streaming-postgres-lab/
│
├── data_generator.py
├── spark_streaming_to_postgres.py
├── postgres_setup.sql
├── user_guide.md
├── data/
│   └── events/
├── checkpoints/
```

---

## Prerequisites

Make sure the following are installed:

* Python (with pandas)
* PostgreSQL
* Apache Spark
* Java

---

# Step-by-Step Instructions

## Step 1: Navigate to Project Folder

```bash id="d2c7q0"
cd /mnt/d/Amalitech/Labs/spark-streaming-postgres-lab
```

---

## Step 2: Start PostgreSQL

```bash id="hsmwb6"
sudo service postgresql start
```

---
## PostgreSQL Setup

## Step 3: Setup Database

Open PostgreSQL:

```bash id="p3hmmv"
sudo -u postgres psql
```

Create and connect to database:

```sql id="i6vpxz"
CREATE DATABASE events_db;
\c events_db
```

Create table:

```sql id="fy59n6"
CREATE TABLE user_events (
    event_id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    event_type VARCHAR(20) NOT NULL,
    product_id INT NOT NULL,
    product_name VARCHAR(100),
    price DECIMAL(10,2),
    event_time TIMESTAMP NOT NULL,
    event_hour INT
);
```

Exit:

```sql id="s1jjyq"
\q
```

---

## Step 4: Start Spark Streaming

```bash id="w8nq9m"
spark-submit \
  --jars postgresql-42.7.3.jar \
  spark_streaming_to_postgres.py
```
Make sure the PostgreSQL JDBC driver (postgresql-42.7.3.jar) is in the project folder.
Wait until you see:

```
Streaming query started...
```

---



## Step 5: Run Data Generator

Open a new terminal and run:

```bash id="2k6u6w"
cd /mnt/d/Amalitech/Labs/spark-streaming-postgres-lab
python3 data_generator.py
```

This will start generating data continuously.

---

## Step 6: Let the System Run

Wait for about **5–10 seconds**.

During this time:

* Data is generated
* Spark processes the data
* Data is stored in PostgreSQL

---

## Step 7: Stop Data Generator

Press:

```
CTRL + C
```

---

## Step 8: Verify Data

Open PostgreSQL:

```bash id="0y9n3o"
sudo -u postgres psql
```

Run:

```sql id="m0p7b9"
\c events_db
SELECT COUNT(*) FROM user_events;
```

You should see a number greater than 0.

---

## Step 9: Stop Spark

Go to the Spark terminal and press:

```
CTRL + C
```

---

## Final Result

If everything works correctly:

* Data is generated
* Data is processed by Spark
* Data is stored in PostgreSQL

---

## Notes

* Always run commands inside the project folder
* Ensure PostgreSQL is running before starting Spark
* Do not stop Spark before verifying data
