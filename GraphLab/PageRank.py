import graphlab as gl


class PageRank:

    work_graph = gl.SGraph
    reset_prob = 0.15
    max_iterations = 30

    def __init__(self, ini_graph):
        self.work_graph = ini_graph

    @staticmethod
    def pr_update(src, edge, dst):
        dst['rank'] += src['prev_rank'] * edge['weight']
        return src, edge, dst

    @staticmethod
    def sum_weight(src, edge, dst):
        src['out_degree'] += 1
        return src, edge, dst

    @staticmethod
    def compute_weight(src, edge, dst):
        if src['out_degree'] == 0:
            src['out_degree'] = 1.0
        edge['weight'] = edge['weight'] / src['out_degree']
        return src, edge, dst

    def run(self):
        self.work_graph.edges['weight'] = 1.0
        self.work_graph.vertices['out_degree'] = 0.0
        self.work_graph = self.work_graph.triple_apply(self.sum_weight, ['out_degree'])
        self.work_graph = self.work_graph.triple_apply(self.compute_weight, ['out_degree', 'weight'])
        self.work_graph.vertices['prev_rank'] = 1.0
        iterations = 0
        while iterations < self.max_iterations:
            self.work_graph.vertices['rank'] = 0.0
            self.work_graph = self.work_graph.triple_apply(self.pr_update, ['rank'])
            self.work_graph.vertices['rank'] = self.reset_prob + self.work_graph.vertices['rank'] * (1 - self.reset_prob)
            self.work_graph.vertices['prev_rank'] = self.work_graph.vertices['rank']
            iterations += 1
        self.work_graph.vertices.remove_columns(['out_degree','prev_rank'])
        return self.work_graph





