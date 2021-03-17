import heapq
from collections import defaultdict

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        grade_dict = defaultdict(list)
        for student, grade in items:
            student_heap = grade_dict[student]
            heapq.heappush(student_heap, grade)
            if len(student_heap) > 5:
                heapq.heappop(student_heap)
        sorted_students = sorted(grade_dict.keys())
        ans = []
        for student in sorted_students:
            ans.append([student, sum(grade_dict[student])//5])
        return ans
