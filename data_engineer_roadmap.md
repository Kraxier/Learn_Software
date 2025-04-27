# Data Engineering and Its Technologies

## 1. Python (Essential)
- **Why**: Dominates data pipelines, ETL (Extract, Transform, Load), and automation.
- **Key Libraries**: 
  - pandas
  - PySpark
  - SQLAlchemy
  - Apache Airflow

## 2. SQL (Non-negotiable)
- **Why**: Querying databases is 50% of data engineering.
- **Focus**:
  - Joins
  - Aggregations
  - Window functions
  - Query optimization

## 3. Bash/Shell Scripting (Bonus)
- **Why**: Automate file operations, cron jobs, and pipeline tasks.

---

## Data Engineering-Specific Concepts

### 1. Data Paradigms

#### A. Batch Processing
- **Tools**: 
  - Apache Spark
  - pandas
  - Airflow
- **Example**: Daily ETL jobs to process logs.

#### B. Stream Processing
- **Tools**: 
  - Apache Kafka
  - Flink
  - Spark Streaming
- **Example**: Real-time fraud detection pipelines.

---

## Data Storage

### A. Databases
- **OLTP (Transactional)**: 
  - PostgreSQL, MySQL
- **OLAP (Analytical)**: 
  - Snowflake, BigQuery, Redshift

### B. Data Lakes
- **Tools**: 
  - S3, Azure Data Lake (store raw/unstructured data)

### C. Data Warehouses
- **Tools**: 
  - BigQuery (structured storage for analytics)

---

## Category | Tools/Techs | Use Case
|-------------|-------------|------------------------------------------|
| **ETL/Orchestration** | Apache Airflow, Luigi, Dagster | Schedule and monitor pipelines. |
| **Big Data** | Apache Spark, Hadoop (HDFS, Hive) | Process large datasets. |
| **Cloud** | AWS (Glue, S3, Redshift), GCP, Azure | Scalable infrastructure. |
| **Data Formats** | Parquet, Avro, JSON, CSV | Efficient storage/serialization. |

---

## Projects to Build

### 1. ETL Pipeline
- **Description**: Scrape web data → Clean → Load to PostgreSQL.

### 2. Data Lake on Cloud
- **Description**: Store raw JSON/CSV in S3 → Query with Athena.

### 3. Real-Time Dashboard
- **Description**: Stream tweets with Kafka → Analyze in real-time.
