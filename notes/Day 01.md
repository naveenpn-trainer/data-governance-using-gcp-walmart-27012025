# Getting Started with Data Management

> Data Management refers to the process of acquiring , storing and maintaining data within an organization

* it involves implementing practices, policies and technologies to ensure that data is accurate , accessible , secure throughout its lifecycle.
* Data Integration, Data Quality, Security, Storage and Analytics

**Key Objectives of Data Management**

1. Data Quality
2. Data Accessibility
3. Data Governance
4. Data Security
5. Regulatory Compliance

## Key Components of Data management process (DMBOK)

> Data Management Body of Knowledge is a framework developed by DAMA international to provide guidance on how to manage data as a organization asset.

* It defines disciplines , practices, and roles required to ensure data is effectively governed , secured, integrationed and utilized to support organizational goals.

![img](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfOPMsO0WL-zf4zg4okByjpcGOulhyOZVdDuizDg0X6b3vlv7_uANVSQP8s2hiNpCOEX_FBv8HbOeYypBLKRRAIxlHExvdCi6UQA0NKdAivp2CsH5MQ8INxE-Y1sEuTWG3LuQ81?key=hVJ-MUwjW6z1Wu69egxFM_X8)

### Foundation Layer : Data Governance layer

> Data Governance provides, policies , roles, standards to ensure data is managed effectively 

**Key Components**

1. Data Quality Management
2. Roles, Policies
3. Data Security
4. Metadata

### Core Operational Layers

1. Data Architecture
   1. Designing the blueprint for how data is structured and flows across systems
2. Data Modeling and Design
   1. Involves creating logical and physical models for data storage in tables
3. Data Storage and Operations
   1. Focuses on storing data securely 
4. Data Security
   1. Protect data from un authorized access.

### Integration and Interoperability Layers

* Designing ETL systems

### Analytical Layers 

These layers focus on extracting information from the data (Decision making, Predictive Analysis)

1. BI 
2. Data Science and ML
3. Metadata Management



**Cloning Git Repo**

```
> cmd
> cd \
> git clone https://github.com/naveenpn-trainer/data-governance-using-gcp-walmart-27012025

```

## Introduction to Big Data

> Big Data refers to the data which is **large, fast** and complex type of **Structured, Semi-Structured and unstructured data** generated from variety of different sources, which **becomes difficult to store and process using a traditional processing system**

Two main challenges w.r.t to Big Data

1. **Storage** : Distributed Storage System
2. **Processing** : MPP (Massive Parallel Processing Framework)

### Hadoop 2.x (Distributed Storage and Processing Framework)

> Apache Hadoop is a **Software framework** that allows us to **Store and Process Large datasets** in parallel and distributed fashion

Hadoop consists of three main components

1. Storage Layer : HDFS (Hadoop Distributed FS)
2. Resource Management Layer : YARN (Yet Another Resource Negotiator)
3. Processing Layer : MapReduce

![img](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcHAqM09cRIkKK6mxQcnkusBnpnPRRjicwKthEddsDwSjlddb28kbtYrGrApZhK350lmuf6vZfWqkytl4YAfQHRGf5apOpaXaDogul2pGRKIgi4HyDkMeGZOuUMrfv4GgNmXK8RtRnRrdk9TlCEobNx21Xt?key=Lcjgu0sLjm8U8i3A_14gRg)

### What is Apache Spark (Distributed Processing Framework)

> Apache Spark is an <mark>in-memory cluster computing framework</mark> designed to handle a wide range of big data workloads.

1. Data Integration and ETL
2. Batch Computation
3. Real-time Streaming
4. ML
5. Graph Computation

* Apache Spark is natively written using **Scala ** programming

### PySpark

> PySpark is the Python API for Apache Spark (Distributed Computing/Processing Framework)

![img](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfhguhUPQ4L8SLLc_HVKwPqlGXnwqa1Zf7y3kFUt-toqxSiyvfNyKSAFyGoJHb38HbiD61pzqw8ko-e41LzO9ftoFkGILtVisf2POyPelaNnmvndRXbU4-e41k3yCpdFHKD2-uBVt7MWzn04Q9djJK5AH62?key=_he-T4Jq934AhrSZa-Be-g)

### Spark Ecosystem

![img](https://lh7-rt.googleusercontent.com/docsz/AD_4nXctu2e-ej9SZpC65NSS8-KlxcwhWUJfZkIDf6a1Yrt6HPoJivYvvgioyYX4CTc4kOdchPoMhEdxg40YVfw9Jk90Q7mtcf4Br0RnGQwFGQgJnb1YBbaBOq20wscC29OvE1nxafBJB667Iodu1bwFlqgNPOaW?key=_he-T4Jq934AhrSZa-Be-g)



### Spark API's for Data Processing

1. Low Level API (RDD's - Deprecated)
2. High Level API - (DataFrame API - )



### Building any Spark Application

In any spark application you perform three steps

1. Load the data.
2. Process the data
3. Write the result to different destination systems

![img](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcf44tDRxxUEIF3V9UH2SKvPJRhvk98uY5sOtdBLjmD2Jt3lrXsj802bGlVz7lG4HiDScEumNvTdipDRZBZAdkjZPHvYsbN88sHrswx7WKD71eFufdnYW_uvZJZICgE6qvTw47t_blu-Zpe_S4TSfTGadI?key=_he-T4Jq934AhrSZa-Be-g)



## What is Spark SQL

> Spark SQL is one of the module in the Spark ecosystem to perform structured and semi-structured (JSON, XML) analysis

## What is Spark DataFrame

> A DataFrame is a distributed collection of data organized into named columns.

* Conceptually we can visualize DF as an in-memory table

![img](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfL30k9twmwk-jfekL6AMvIKeQBiJ5OKPuOv3cpqaAsuOmoje5esme21Eu6efGScQf324QmoZEki_zcP8d7NLGqXlxZikw6n2bekjjgJA3ZgC4gCX_0_8keMz6spnV0Fr0CzZzJZXdqyYXNMmTptNMavbjT?key=yGW25KMloT80Lch6YWjT9A)



### Databricks

> Databricks is a unified cloud platform (Google Cloud, Azure) which can be used by Data Engineering, Data Analyst, Data Scientist

* Databricks uses Apache Spark as Runtime









