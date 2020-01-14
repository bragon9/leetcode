from collections import deque

class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        ans = [0] * len(T)
        if len(T) == 1:
            return ans
        # Stack that holds a tuple (temp, day) sorted by temp desc.
        hold_arr = deque()
        for curr_index, curr_temp in enumerate(T[:-1]):
            next_index = curr_index + 1
            next_temp = T[next_index]
            # Tomorrow is hotter than today.
            if next_temp > curr_temp:
                ans[curr_index] = 1
                # Check to see if tomorrow is hotter than the last (coldest) day in the hold_arr.
                while hold_arr:
                    # If it is, pop off the value and fill in the index into ans.
                    if hold_arr[-1][0] < next_temp:
                        hold_temp, hold_index = hold_arr.pop()
                        ans[hold_index] = next_index - hold_index
                    else:
                        break
            # Tomorrow is cooler, append today in the hold_arr.
            else:
                hold_arr.append((curr_temp, curr_index))
        return ans
