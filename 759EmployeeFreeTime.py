class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        sorted_sched = []
        for employee_sched in schedule:
            for interval in employee_sched:
                sorted_sched.append((interval.start, interval.end))
        sorted_sched.sort(key=lambda x:(x[0], -x[1]))
        ptr = 1
        while ptr < len(sorted_sched):
            curr_start, curr_end = sorted_sched[ptr]
            prev_start, prev_end = sorted_sched[ptr-1]
            if prev_start <= curr_start <= prev_end:
                if curr_end > prev_end:
                    sorted_sched[ptr-1] = (prev_start, curr_end)
                sorted_sched.pop(ptr)
            else:
                ptr += 1
        ans = []
        for i in range(len(sorted_sched)-1):
            ans.append(Interval(sorted_sched[i][1], sorted_sched[i+1][0]))
        return ans
