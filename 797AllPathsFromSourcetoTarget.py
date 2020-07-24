class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.end = len(graph)-1
        self.adj_dict = {}
        for src in range(len(graph)):
            self.adj_dict[src] = graph[src]
        self.ans = []
        self.dead = set()
        self.walk(0, [])
        return self.ans
    
    def walk(self, node, path):
        if node == self.end:
            self.ans.append(path+[node])
        if node in self.dead:
            return
        if (node not in self.adj_dict) or not(self.adj_dict[node]):
            self.dead.add(node)
            return
        for dest in self.adj_dict[node]:
            self.walk(dest, path + [node])
