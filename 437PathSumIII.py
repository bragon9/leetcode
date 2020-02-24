class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.paths = 0
        self.total = sum
        if not(root):
            return 0
        self.get_paths(root, [0])
        return self.paths
    
    def get_paths(self, node, path_sum_arr):
        for index, value in enumerate(path_sum_arr):
            new_total = value + node.val
            if new_total == self.total:
                self.paths += 1
            path_sum_arr[index] = new_total
        if node.left:
            self.get_paths(node.left, path_sum_arr + [0])
        if node.right:
            self.get_paths(node.right, path_sum_arr + [0])
