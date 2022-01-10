# GeoPregel

[Apache Giraph](https://giraph.apache.org/) is an iterative graph processing system built for high scalability. GeoPregel is based on giraph, and optimizes the communication framework. With the use of differential privacy to ensure privacy security, the graph computation has a high accuracy while using lower WAN.

(可以加abstraction)

## Getting Started
You will need the following:
- Java 1.8 or higher
- Maven 3 or higher
- Hadoop 2

Build:
```bash
git clone https://github.com/TanHaobin/GeoPregel.git
cd GeoPregel
mvn -Phadoop_2 -DskipTests clean package
```
## Pagerank Sample
GeoPregel's launch is similar to giraph's, which can be viewed in [Giraph - Quick Start](https://giraph.apache.org/quick_start.html). 

Example:

```bash
hadoop jar ${GIRAPH_HOME}/geo-pregel-examples/target/geo-pregel-examples-1.4.0-SNAPSHOT-for-hadoop-2.5.1-jar-with-dependencies.jar org.apache.giraph.GiraphRunner org.apache.giraph.examples.SimplePageRankComputation  -vif org.apache.giraph.io.formats.JsonLongDoubleFloatDoubleVertexInputFormat  -vip /input/livejournal -vof org.apache.giraph.io.formats.IdWithValueTextOutputFormat -op /output -w 5 -ca mapred.job.tracker=master,privacyLabelPerWorker="2 3 1 3 3",Iteration=20,pagerankLowerBound=0.15,pagerankUppererBound=500,samplingRate=0.8  -mc org.apache.giraph.examples.SimplePageRankComputation\$SimplePageRankMasterCompute
```


Among other things, GeoPregel requires -w (the number of workers in hadoop) as the actual number of machines, which represent datacenter in our papre. The other Privacy-related parameters are in -ca, as follows.
- privacyLabelPerWorker: Represent each worker's privacy label. The higher the label means the tighter privacy policy.
- Iteration: The iteration of Pagerank algorithm.
- pagerankLowerBound: The lower bound of rank value in pagerank algorithm.
- pagerankUppererBound: The upper bound of rank value in pagerank algorithm.
- privacyBudget: The privacy budget which represent the privacy level(i.e., the lower the privacy budget, the higher privacy protect).
- samplingRate: The sampling rate of messages remained during inter-DC communication, within 0.0 to 1.0.
