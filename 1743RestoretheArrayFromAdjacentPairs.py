class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        # Build adjacency dictionary
        adj_dict = collections.defaultdict(list)
        for i, j in adjacentPairs:
            adj_dict[i].append(j)
            adj_dict[j].append(i)
        # Find one of the ends
        for edge, connections in adj_dict.items():
            if len(connections) == 1:
                start = edge
                break
        # DFS
        visited = set()
        ans = []
        to_visit = [start]
        while to_visit:
            curr = to_visit.pop()
            visited.add(curr)
            ans.append(curr)
            for neighbor in adj_dict[curr]:
                if neighbor not in visited:
                    to_visit.append(neighbor)
        return ans
            
