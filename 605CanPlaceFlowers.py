class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        ans = 0
        # True, once we have encountered a "full" flowerpot
        sandwich = False
        for pot in flowerbed:
            if pot == 0:
                count += 1
            else:
                if sandwich:
                    if count:
                        ans += count//2 - (count+1)%2
                else:
                    sandwich = True
                    if count:
                        ans += count//2 
                count = 0
            if ans >= n:
                return True
        if count:
            if sandwich:
                ans += count//2
            else:
                ans += count//2 + count%2
        return ans >= n
                
