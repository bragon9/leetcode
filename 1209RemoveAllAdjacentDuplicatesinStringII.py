from collections import deque

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        s_arr = list(s)
        while True:
            remove = False
            stack = deque()
            for letter in s_arr:
                if not(stack):
                    stack.append([letter, 1])
                else:
                    if stack[-1][0] == letter:
                        stack[-1][1] += 1
                        if stack[-1][1] >= k:
                            remove = True
                            stack.pop()
                    else:
                        stack.append([letter, 1])
            s_arr = [i[0]*i[1] for i in stack]
            if not(remove):
                return ''.join(s_arr)
                
        
        
            
                            
