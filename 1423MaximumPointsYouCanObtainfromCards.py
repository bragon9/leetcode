class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total = 0
        ans = 0
        # Get initial sum if we take all from the left
        for i in range(k):
            total += cardPoints[i]
        # If we have to take all cards, return answer
        if k == len(cardPoints):
            return total
        ans = total
        l = k
        r = 0
        # Move a sliding window until we take all from the right
        for _ in range(k):
            l -= 1
            r -= 1
            # Subtract number from left side, add number from right side
            total -= cardPoints[l]
            total += cardPoints[r]
            ans = max(ans, total)
        return ans
