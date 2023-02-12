
# Welcome to PGPregel



PGPregel is an end-to-end system that provides privacy-preserving graph processing in geo-distributed DCs with low latency and high utility.  To ensure privacy, PGPregel smartly integrates Differential Privacy into graph processing systems to preserve good utility and low latency. PGPregel employs two core techniques, namely sampling and combiners to improve the accuracy of processing results and to reduce the amount of inter-DC data communications while preserving high utility. We implement our design based on the [Giraph](https://giraph.apache.org/) system.

# Getting Started

## Dependency:

- Java 1.8 or higher
- Maven 3 or higher
- Hadoop 2

## Deploying Hadoop

See [Giraph - Deploying Hadoop](https://giraph.apache.org/quick_start.html#qs_section_2). 

## Deploying PGPregel

Make sure that all the dependencies are installed and that the versions of dependencies rely on meet the requirements, then you need to run the following commands:

```bash
git clone https://github.com/PGPregel/PGPregel.git
cd PGPregel
mvn -Phadoop_2 -DskipTests clean package
```

# Running an example

```bash
hadoop jar PGPregel/geo-pregel-examples/target/geo-pregel-examples-1.4.0-SNAPSHOT-for-hadoop-2.5.1-jar-with-dependencies.jar org.apache.giraph.GiraphRunner org.apache.giraph.examples.SimplePageRankComputation  -vif org.apache.giraph.io.formats.JsonLongDoubleFloatDoubleVertexInputFormat  -vip /livejournal_json -vof org.apache.giraph.io.formats.IdWithValueTextOutputFormat -op /output -w 5 -ca mapred.job.tracker=localhost,privacyLabelPerWorker="2 3 1 3 3",pagerankIteration=20,pagerankLowerBound=0.15,pagerankUppererBound=500,samplingRate=0.8  -mc org.apache.giraph.examples.SimplePageRankComputation\$SimplePageRankMasterCompute
```


PGPregel requires -w (the number of workers in hadoop) as the actual number of machines, which represent datacenter in our papre. The other Privacy-related parameters are in -ca, as follows.

- privacyLabelPerWorker: Represent each worker's privacy label. The higher the label means the tighter privacy policy.
- Iteration: The iteration of Pagerank algorithm.
- pagerankLowerBound: The lower bound of rank value in pagerank algorithm.
- pagerankUppererBound: The upper bound of rank value in pagerank algorithm.
- privacyBudget: The privacy budget which represent the privacy level(i.e., the lower the privacy budget, the higher privacy protect).
- samplingRate: The sampling rate of messages remained during inter-DC communication, within 0.0 to 1.0. 

# To cite PGPregel, please use:
[PDF](https://github.com/PGPregel/PGPregel/raw/master/PGPregel_SoCC22.pdf)


Amelie Chi Zhou, Ruibo Qiu, Thomas Lambert, Tristan Allard, Shadi Ibrahim, Amr El Abbadi:
PGPregel: an end-to-end system for privacy-preserving graph processing in geo-distributed data centers. SoCC 2022: 386-402
