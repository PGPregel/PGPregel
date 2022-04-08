
# More information

[Click](https://github.com/GeoPregel/GeoPregel/blob/master/technical%20report/GeoPregel_SC22.pdf) to see the technical report which could get more information about the project.

# Welcome to GeoPregel

GeoPregel is an end-to-end system that provides privacy-preserving graph processing in geo-distributed DCs with low latency and high utility.  To ensure privacy, GeoPregel smartly integrates Differential Privacy into graph processing systems to preserve good utility and low latency. GeoPregel employs two core techniques, namely sampling and combiners to improve the accuracy of processing results and to reduce the amount of inter-DC data communications while preserving high utility. We implement our design based on the [Giraph](https://giraph.apache.org/) system.

# Getting Started

## Dependency:

- Java 1.8 or higher
- Maven 3 or higher
- Hadoop 2

## Deploying Hadoop

See [Giraph - Deploying Hadoop](https://giraph.apache.org/quick_start.html#qs_section_2). 

## Deploying GeoPregel

Make sure that all the dependencies are installed and that the versions of dependencies rely on meet the requirements, then you need to run the following commands:

```bash
git clone https://github.com/TanHaobin/GeoPregel.git
cd GeoPregel
mvn -Phadoop_2 -DskipTests clean package
```

# Running an example

```bash
hadoop jar GeoPregel/geo-pregel-examples/target/geo-pregel-examples-1.4.0-SNAPSHOT-for-hadoop-2.5.1-jar-with-dependencies.jar org.apache.giraph.GiraphRunner org.apache.giraph.examples.SimplePageRankComputation  -vif org.apache.giraph.io.formats.JsonLongDoubleFloatDoubleVertexInputFormat  -vip /input/livejournal_not_map -vof org.apache.giraph.io.formats.IdWithValueTextOutputFormat -op /output -w 5 -ca mapred.job.tracker=master,privacyLabelPerWorker="2 3 1 3 3",Iteration=20,pagerankLowerBound=0.15,pagerankUppererBound=500,samplingRate=0.8  -mc org.apache.giraph.examples.SimplePageRankComputation\$SimplePageRankMasterCompute
```


GeoPregel requires -w (the number of workers in hadoop) as the actual number of machines, which represent datacenter in our papre. The other Privacy-related parameters are in -ca, as follows.

- privacyLabelPerWorker: Represent each worker's privacy label. The higher the label means the tighter privacy policy.
- Iteration: The iteration of Pagerank algorithm.
- pagerankLowerBound: The lower bound of rank value in pagerank algorithm.
- pagerankUppererBound: The upper bound of rank value in pagerank algorithm.
- privacyBudget: The privacy budget which represent the privacy level(i.e., the lower the privacy budget, the higher privacy protect).
- samplingRate: The sampling rate of messages remained during inter-DC communication, within 0.0 to 1.0. 
