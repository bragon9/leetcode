class Solution:
    def sortString(self, s: str) -> str:
        ans = []
        # List of all characters in s
        char_set = set()
        # Count of all chars in s
        char_dict = {}
        for char in s:
            char_set.add(char)
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
        if len(char_set) == 1 or len(s) == 1:
            return s
        # sort all chars in s
        char_list = sorted(list(char_set))
        ans = []
        forward = True
        # Loop through forwards/backwards and use up all chars
        while len(ans) < len(s):
            if forward:
                for i in range(len(char_list)):
                    char = char_list[i]
                    if char_dict[char] > 0:
                        ans.append(char)
                        char_dict[char] -= 1
            else:
                for i in range(len(char_list)-1, -1, -1):
                    char = char_list[i]
                    if char_dict[char] > 0:
                        ans.append(char)
                        char_dict[char] -= 1
            forward = not(forward)
        return ''.join(ans)
