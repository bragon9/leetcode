class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        adj_dict = {i:[] for i in range(len(isConnected))}
        for start_city, entry in enumerate(isConnected):
            for city_index, value in enumerate(entry):
                if value == 1 and city_index != start_city:
                    adj_dict[start_city].append(city_index)
        ans = 0
        visited = set()
        for city in adj_dict.keys():
            if city in visited:
                continue
            visited.add(city)
            ans += 1
            to_visit = []
            for neighbor in adj_dict[city]:
                if neighbor not in visited:
                    to_visit.append(neighbor)
            while to_visit:
                neighbor = to_visit.pop()
                visited.add(neighbor)
                for indirect_neighbor in adj_dict[neighbor]:
                    if indirect_neighbor not in visited:
                        to_visit.append(indirect_neighbor)            
        return ans
