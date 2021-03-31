class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        adj_dict = {i:[] for i in range(1,n+1)}
        in_dict = {i:0 for i in range(1, n+1)}
        for a, b in relations:
            adj_dict[a].append(b)
            in_dict[b] += 1
        available_courses = [k for k,v  in in_dict.items() if v == 0]
        semesters = 0
        courses_taken = 0
        while available_courses:
            next_semester = []
            semesters += 1
            for curr_course in available_courses:
                courses_taken += 1
                for next_course in adj_dict[curr_course]:
                    in_dict[next_course] -= 1
                    if in_dict[next_course] == 0:
                        next_semester.append(next_course)
            available_courses = next_semester
        if courses_taken == n:
            return semesters
        else:
            return -1
