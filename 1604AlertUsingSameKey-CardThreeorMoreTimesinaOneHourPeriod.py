from bisect import insort

class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        ans = []
        time_dict = defaultdict(list)
        for i in range(len(keyName)):
            hours, minutes = keyTime[i].split(':')
            seconds = 3600 * int(hours) + 60 * int(minutes)
            insort(time_dict[keyName[i]], seconds)
        for name, times in time_dict.items():
            if len(times) < 3:
                continue
            for i in range(len(times)-2):
                if times[i+2] - times[i] <= 3600:
                    insort(ans, name)
                    break
        return ans
