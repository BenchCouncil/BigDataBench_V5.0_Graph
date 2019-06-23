__author__ = 'sunny'


import graphlab as gl
from graphlab import SFrame





class ConnectedComponent:
    work_graph = gl.SGraph

    def __init__(self, ini_graph):
        self.work_graph = ini_graph

    @staticmethod
    def cc_update(src, edge, dst):
        src_label = src['label']
        dst_label = dst['label']
        if src_label < dst_label:
            dst['label'] = src_label
            dst['changed'] = True
        elif src_label > dst_label:
            src['label'] = dst_label
            src['changed'] = True
        return src, edge, dst

    def run(self):
        self.work_graph.vertices['label'] = self.work_graph.vertices['__id']
        num_changed = len(self.work_graph.vertices)
        while num_changed > 0:
            self.work_graph.vertices['changed'] = False
            self.work_graph = self.work_graph.triple_apply(self.cc_update, ['label', 'changed'])
            num_changed = self.work_graph.vertices['changed'].sum()
        self.work_graph.vertices.remove_column('changed')
        return self.work_graph
