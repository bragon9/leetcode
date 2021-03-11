from collections import defaultdict

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_dict = defaultdict(list)
        for edge1, edge2 in edges:
            adj_dict[edge1].append(edge2)
            adj_dict[edge2].append(edge1)
        ans = 0
        visited = set()
        for i in range(n):
            if i in visited:
                continue
            ans += 1
            visited.add(i)
            to_visit = adj_dict[i]
            while to_visit:
                nxt = to_visit.pop()
                visited.add(nxt)
                for neighbor in adj_dict[nxt]:
                    if neighbor not in visited:
                        to_visit.append(neighbor)
        return ans
