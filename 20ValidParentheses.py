from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        open_chars = set(['(', '{', '['])
        for i in s:
            if i in open_chars:
                stack.append(i)
            else:
                if stack:
                    last_open = stack.pop()
                    if i == ')':
                        if last_open != '(':
                            return False
                    if i == '}':
                        if last_open != '{':
                            return False
                    if i == ']':
                        if last_open != '[':
                            return False
                else:
                    return False
        return not(stack)
                             
