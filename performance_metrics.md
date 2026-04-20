# Performance Metrics

## Overview

This document evaluates the performance of the real-time data streaming pipeline.

It focuses on throughput, latency, and system stability during execution.

---

## System Configuration

* Batch size: ~1000 rows per file
* Data generation rate: 1 batch per second
* Processing framework: Apache Spark Structured Streaming
* Storage: PostgreSQL

---

## Results
The performance metrics were obtained from the Spark streaming logs during execution.

### 🔹 Total Data Processed

* More than **110,000 rows** were successfully processed and stored.

---

### 🔹 Throughput

* Average throughput: **Approximately 500 – 2000 rows per second depending on system performance**
* Throughput depends on system resources and batch processing time

---

### 🔹 Latency

* Average latency per batch: **1 – 2 seconds**
* Data is processed shortly after being generated

---

## Observations

* Spark processed data continuously without failure
* PostgreSQL successfully stored all incoming data
* No data loss was observed during execution
* The system remained stable during streaming
* The system handled continuous data input without delays or bottlenecks

---

## Performance Insights

* Atomic file writes ensured Spark did not read incomplete files
* Checkpointing enabled recovery and fault tolerance
* Batch processing improved efficiency and stability

---

## Conclusion

The system demonstrates:

* High throughput
* Low latency
* Reliable streaming

This confirms that the pipeline is efficient, scalable, and suitable for real-time data processing applications.
