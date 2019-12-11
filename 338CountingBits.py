class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        arr = []
        for i in range(num+1):
            bin_num = "{0:b}".format(i)
            arr.append(bin_num.count('1'))
        return arr
