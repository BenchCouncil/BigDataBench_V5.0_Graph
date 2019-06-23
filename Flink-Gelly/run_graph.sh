FLINK_HOME=/home/L/flink-0.10.0
INPUT_PATH=hdfs://hw005:9000/Connect-data/Facebook_genGragh_2.txt
OUTPUT_PATH=hdfs://hw005:9000/flink-graph-out
ALGO=cc
hadoop dfs -rm -r /flink-graph-out
echo "Choose the algorithm to run: "
echo "bfs cc pr lp tc"
read ALGO
if [ $ALGO == "bfs" ]; then
echo "running bfs now"
SOURCE=0
time $FLINK_HOME/bin/flink run graph-flink.jar $INPUT_PATH $OUTPUT_PATH bfs $SOURCE  

elif [ $ALGO == "cc" ]; then
echo "running connected components now"
time $FLINK_HOME/bin/flink run graph-flink.jar $INPUT_PATH $OUTPUT_PATH cc

elif [ $ALGO == "pr" ]; then
ITERATIONS=10
RESETPROB=0.15
echo "running pagerank now"
time $FLINK_HOME/bin/flink run graph-flink.jar $INPUT_PATH $OUTPUT_PATH pr $ITERATIONS $RESETPROB

elif [ $ALGO == "lp" ]; then
ITERATIONS=10
echo "running label propagation now"
time $FLINK_HOME/bin/flink run graph-flink.jar $INPUT_PATH $OUTPUT_PATH lp $ITERATIONS

elif [ $ALGO == "tc" ]; then
echo "running triangle count now"
time $FLINK_HOME/bin/flink run graph-flink.jar $INPUT_PATH $OUTPUT_PATH tc

fi
