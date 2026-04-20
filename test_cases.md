# Test Cases

## Overview

This document describes the manual test cases used to verify that the real-time data pipeline works correctly.

Each test includes the expected result and the actual result.

---

## Test Case 1: Data Generator Starts

**Description:**
Run the data generator script.

**Command:**

```bash
python3 data_generator.py
```

**Expected Result:**
CSV files are continuously created in `data/events/`.

**Actual Result:**
CSV files were successfully generated.

**Status:** PASS

---

## Test Case 2: Spark Streaming Starts

**Description:**
Start the Spark streaming application.

**Command:**

```bash
spark-submit \
  --jars postgresql-42.7.3.jar \
  spark_streaming_to_postgres.py
```

**Expected Result:**
Spark starts successfully and displays "Streaming query started...".

**Actual Result:**
Spark streaming started successfully.

**Status:** PASS

---

## Test Case 3: Data Processing

**Description:**
Verify that Spark reads and processes CSV files.

**Expected Result:**
Data is cleaned and transformed (event_time and event_hour are created).

**Actual Result:**
Data was cleaned and transformed, and new columns (event_time and event_hour) were created.

**Status:** PASS

---

## Test Case 4: Data Stored in PostgreSQL

**Description:**
Check if processed data is inserted into PostgreSQL.

**Command:**

```sql
SELECT COUNT(*) FROM user_events;
```

**Expected Result:**
Row count increases as new data is processed.

**Actual Result:**
**Actual Result:**
More than 100,000 rows were inserted. The row count increased over time as streaming continued.

**Status:** PASS

---

## Test Case 5: Continuous Streaming

**Description:**
Verify that the system runs continuously.

**Expected Result:**
New data is continuously processed and stored.

**Actual Result:**
System processed data continuously without interruption.

**Status:** PASS

---

## Test Case 6: Checkpoint Recovery

**Description:**
Stop and restart the Spark streaming application.

**Expected Result:**
Spark resumes processing from the last checkpoint without data loss.

**Actual Result:**
Spark resumed successfully using checkpoint data.

**Status:** PASS

---

## Conclusion

All test cases passed successfully, confirming that the pipeline works as expected for real-time data processing.
