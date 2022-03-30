class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        sorted_births = sorted([x[0] for x in logs])
        sorted_deaths_desc = sorted([x[1] for x in logs], reverse=True)
        
        ans = 0
        curr_pop = 0
        max_pop = 0
        
        for birth_year in sorted_births:
            curr_pop += 1
            
            while sorted_deaths_desc and sorted_deaths_desc[-1] <= birth_year:
                sorted_deaths_desc.pop()
                curr_pop -= 1
                
            if curr_pop > max_pop:
                max_pop = curr_pop
                ans = birth_year
                
        return ans
