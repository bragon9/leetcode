class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        self.arr = arr
        # Key = index, value = [bool, bool] for if we have gone left/right from this index
        self.visited_dict = {i:[False,False] for i in range(len(arr))}
        if self.jump(start):
            return True
        else:
            return False
        
    def jump(self, index):
        # Don't accept invalid indexes
        if index < 0 or index >= len(self.arr):
            return
        if self.arr[index] == 0:
            return True
        L, R = self.visited_dict[index]
        if not(L) and not(R):
            self.visited_dict[index] = [True,True]
            return self.jump(index-self.arr[index]) or self.jump(index+self.arr[index])
        elif not(L):
            self.visited_dict[index][0] = True
            return self.jump(index-self.arr[index])
        elif not(R):
            self.visited_dict[index][1] = True
            return self.jump(index+self.arr[index])
