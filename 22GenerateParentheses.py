from collections import deque

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.ans = deque()
        sub_ans = deque()
        sub_ans.append('(')
        self.permuteParentheses(n-1, n, sub_ans)
        return self.ans
        
    def permuteParentheses(self, open_left, close_left, sub_ans):
        local_ans_open = sub_ans.copy()
        local_ans_close = sub_ans.copy()
        local_ans_open.append('(')
        local_ans_close.append(')')
        # If we have used all opens and closes, return the answer.
        if not(open_left) and not(close_left):
            self.ans.append(''.join(sub_ans))
            return
        # You can always use open
        if open_left:
            self.permuteParentheses(open_left-1, close_left, local_ans_open)
        # You can only insert close if we have used that many opens.
        if close_left > open_left:
            self.permuteParentheses(open_left, close_left-1, local_ans_close)
        
