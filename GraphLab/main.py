__author__ = 'sunny'

import graphlab as gl
import BreadthFirstSearch as bfs
import ConnectedComponent as cc
import PageRank as pr
import TriangleCount as tc
import time

file_path = raw_input("file input path:\t")
save_path = raw_input("result save path:\t")
algorithms = raw_input("choose algorithms:\t")
flag = raw_input("distrib?Y/N:\t")
if(flag == 'Y'):
    user_dato_dist_path = raw_input("dato_dist_path:\t")
    user_hadoop_conf_dir = raw_input("hadoop_conf_dir:\t")
start = time.time()
params = algorithms.split(' ')
ini_graph = gl.load_sgraph(file_path, 'snap', ' ')

def graphlab_distrib( param , work_graph):
    algorithm = None

    if param[0] == 'bfs':
        algorithm = bfs.BreadhFirstSearch(work_graph)
        if len(param) > 1:
            algorithm.source_vertex = int(param[1])
    elif param[0] == 'pr':
        algorithm = pr.PageRank(work_graph)
        if len(param) > 1:
            algorithm.max_iterations = int(param[1])
        if len(param) > 2:
            algorithm.reset_prob = float(param[2])
    elif param[0] == 'cc':
        algorithm = cc.ConnectedComponent(work_graph)
    elif param[0] == 'tc':
        algorithm = tc.TriangleCount(work_graph)
    # elif param[0] == 'lp':
    #     algorithm = lp.LabelPropagation(work_graph)
    #     if len(param) > 1:
    #         algorithm.max_iterations = int(param[1])
    else:
        print("error algorithm input!")

    resultGraph = algorithm.run()
    return resultGraph

if(flag == 'Y'):

    c = gl.deploy.hadoop_cluster.create(
        name='graphlab-cluster',
        dato_dist_path=user_dato_dist_path,
        hadoop_conf_dir=user_hadoop_conf_dir
    )
    # c has been created or loaded before
    job = gl.deploy.job.create(graphlab_distrib, environment=c, param=params, work_graph=ini_graph)

    graph = job.get_results()

elif(flag == 'N'):

    graph = graphlab_distrib(params, ini_graph)
else:
    print("distrib choose error")
    exit(0)

graph.vertices.save(save_path + "/" + params[0] + "_result" + str(start), 'csv')
f = open(save_path + "/" + params[0] + "_runTime" + str(start), 'w')
end = time.time() - start
f.write("run time: " + str(end) + "ms")

