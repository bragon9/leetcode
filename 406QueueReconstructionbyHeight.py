class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        sorted_people = sorted(people, key = lambda x: (x[0]*-1, x[1]))
        ans_arr = []
        for i in sorted_people:
            ans_arr.insert(i[1], i)
        return (ans_arr)
