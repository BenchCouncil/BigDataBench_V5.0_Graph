__author__ = 'sunny'
import graphlab as gl




class TriangleCount:
    work_graph = gl.SGraph
    def __init__(self, ini_graph):
        self.work_graph = ini_graph

    def run(self):

        tc = gl.triangle_counting.create(self.work_graph)
        self.work_graph.vertices['triangle_count'] = tc['graph'].vertices['triangle_count']
        return self.work_graph
