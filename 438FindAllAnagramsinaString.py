class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        if len(p) > len(s):
            return ans
        # Walk through until we find one anagram.
        ptr = 0
        while ptr < len(s):
            # Start index of first anagram.
            first_index = self.find_first_anagram(p, s, ptr)
            if first_index == -1:
                return ans
            ans.append(first_index)
            # Set pointer to the end of the anagram, and we can check incrementally now.
            ptr = first_index + len(p) 
            # Check anagram one index at a time until it fails.
            while True:
                # Start is the beginning of the anagram we are testing.
                start = ptr - len(p) + 1
                if ptr < len(s) and s[ptr] == s[start - 1]:
                    # The letter we are taking out by sliding the window over 1 == new letter
                    ans.append(start)
                    ptr += 1
                # The new letter breaks the anagram, resume testing by the whole string, p, from start index.
                else:
                    ptr = start 
                    break
            ptr += 1
        return ans
       
    def create_word_dict(self, p):
        p_dict = {}
        for letter in p:
            if letter not in p_dict:
                p_dict[letter] = 1
            else:
                p_dict[letter] += 1
        return p_dict
            
    def find_first_anagram(self, p, s, ptr):
        p_dict = self.create_word_dict(p)
        while ptr < len(s):
            value = s[ptr]
            if value in p_dict:
                s_dict = {value:1}
                # Check to see if there is enough room left in S.
                if ptr+len(p) <= len(s):
                    # Check from the current index to index + len(p)
                    for i in range(ptr+1, ptr+len(p)):
                        letter = s[i]
                        # If the letter is in p, put it into s_dict
                        if letter in p_dict:
                            if letter in s_dict:
                                s_dict[letter] += 1
                                # If there are more of this letter in s, then we can stop.
                                if s_dict[letter] > p_dict[letter]:
                                    break
                            else:
                                s_dict[s[i]] = 1
                        # Letter is not in p, stop.
                        else:
                            ptr = i
                            break
                    # If s_dict == p_dict, this index is the start of an anagram of p.
                    if s_dict == p_dict:
                        return ptr
            ptr += 1
        return -1 
            

