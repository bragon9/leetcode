from bisect import bisect

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        dig_logs = []
        let_logs = []
        for log in logs:
            for index, value in enumerate(log):
                if value == ' ':
                    ident = log[:index]
                    s = log[index+1:]
                    break
            if s[-1].isnumeric():
                dig_logs.append(log)
            else:
                let_logs.insert(bisect(let_logs, [s, ident]), [s, ident])
        ans = []
        for log in let_logs:
            ans.append(f'{log[1]} {log[0]}')
        ans.extend(dig_logs)
        return ans
                
