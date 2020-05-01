# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        lo = 1
        hi = n
        while True:
            mid = (lo + hi) // 2
            # Mid version was bad.
            if isBadVersion(mid):
                # If the version before it was good, it's the answer.
                if not(isBadVersion(mid-1)):
                    return mid
                else:
                    hi = mid
            # Mid version was good.
            else:
                # If the version after it is bad, that is the answer.
                if (isBadVersion(mid+1)):
                    return mid+1
                else:
                    lo = mid
            
                    
