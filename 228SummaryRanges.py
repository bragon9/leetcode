class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not(nums):
            return []
        if len(nums) == 1:
            return [str(nums[0])]
        TO_CHAR = '->'
        ans = []
        sub_ans = []
        for i, num in enumerate(nums):
            if i > 0:
                prev = nums[i-1]
            else:
                prev = None
            if i < len(nums)-1:
                next = nums[i+1]
            else:
                next = None
            if prev == None:
                sub_ans.append(str(num))
            else:
                # If the number is not next in the sequence.
                if num != prev+1:
                    if len(sub_ans) == 1:
                        ans.extend(sub_ans)
                        sub_ans = [str(num)]
                    else:
                        ans.append(TO_CHAR.join(sub_ans))
                        sub_ans = [str(num)]
                    if next == None:
                        ans.append(str(num))
                # The number is the next in the sequence.
                else:
                    if not(sub_ans):
                        sub_ans.append(str(num))
                    elif len(sub_ans) == 1:
                        sub_ans.append(str(num))
                    else:
                        sub_ans[-1] = str(num)
                    if next == None:
                        if len(sub_ans) == 1:
                            ans.extend(sub_ans)
                        else:
                            ans.append(TO_CHAR.join(sub_ans))
        return ans
                    
                    
            
