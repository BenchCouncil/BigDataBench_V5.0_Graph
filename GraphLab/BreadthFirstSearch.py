__author__ = 'sunny'

import graphlab as gl
from graphlab import SFrame


max_value = 1e30

class BreadthFirstSearch:

    work_graph = gl.SGraph
    source_vertex = 1

    def __init__(self, ini_graph):
        self.work_graph = ini_graph

    @staticmethod
    def bfs_update(src, edge, dst):
        src_label = src['label']
        dst_label = dst['label']
        if (src_label < max_value) and (src_label + 1 < dst_label):
            dst['label'] = src_label + 1
            dst['changed'] = True
        return src, edge, dst

    def run(self):
        self.work_graph.vertices['label'] = map(lambda x: max_value if x != self.source_vertex else 0.0,
                                                self.work_graph.vertices['__id'])
        num_changed = len(self.work_graph.vertices)
        while num_changed > 0:
            self.work_graph.vertices['changed'] = False
            self.work_graph = self.work_graph.triple_apply(self.bfs_update, ['label', 'changed'])
            num_changed = self.work_graph.vertices['changed'].sum()
        self.work_graph.vertices.remove_column('changed')
        return self.work_graph
