SPARK_HOME=/home/L/spark-1.5.1-bin-hadoop2.6
INPUT_PATH=hdfs://hw005:9000/Connect-data/Facebook_genGragh_3.txt
OUTPUT_PATH=hdfs://hw005:9000/spark-graph-out
ALGO=cc
hadoop dfs -rm -r /spark-graph-out
echo "Choose the algorithm to run: "
echo "bfs cc pr lp tc"
read ALGO
if [ $ALGO == "bfs" ]; then
echo "running bfs now"
SOURCE=0
time $SPARK_HOME/bin/spark-submit graph-spark.jar $INPUT_PATH $OUTPUT_PATH bfs $SOURCE  

elif [ $ALGO == "cc" ]; then
echo "running connected components now"
time $SPARK_HOME/bin/spark-submit graph-spark.jar $INPUT_PATH $OUTPUT_PATH cc

elif [ $ALGO == "pr" ]; then
ITERATIONS=10
RESETPROB=0.15
echo "running pagerank now"
time $SPARK_HOME/bin/spark-submit graph-spark.jar $INPUT_PATH $OUTPUT_PATH pr $ITERATIONS $RESETPROB

elif [ $ALGO == "lp" ]; then
ITERATIONS=10
echo "running label propagation now"
time $SPARK_HOME/bin/spark-submit graph-spark.jar $INPUT_PATH $OUTPUT_PATH lp $ITERATIONS

elif [ $ALGO == "tc" ]; then
echo "running triangle count now"
time $SPARK_HOME/bin/spark-submit graph-spark.jar $INPUT_PATH $OUTPUT_PATH tc

fi
