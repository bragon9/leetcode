class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        processed = set()
        copy_dict = {}
        if not(node):
            return None
        ans = None
        to_copy = [node]
        first = False
        while to_copy:
            original = to_copy.pop()
            if original.val in processed:
                continue
            if original.val not in copy_dict:
                new_node = Node(original.val)
                copy_dict[original.val] = new_node
            else:
                new_node = copy_dict[original.val]
            for neighbor in original.neighbors:
                if neighbor not in new_node.neighbors:
                    if neighbor.val not in copy_dict:
                        neighbor_node = Node(neighbor.val)
                        copy_dict[neighbor.val] = neighbor_node
                    else:
                        neighbor_node = copy_dict[neighbor.val]
                    new_node.neighbors.append(neighbor_node)
                to_copy.append(neighbor)
            processed.add(original.val)
            if not(first):
                ans = new_node
                first = True
        return ans
