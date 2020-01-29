class Solution:
    def countSubstrings(self, s: str) -> int:
        self.is_palindrome = set()
        ans = 0
        # Loop through all possible substrings
        for i in range(len(s), 0, -1):
            for start_index in range(len(s)):
                if (i + start_index) <= len(s):
                    current_str = s[start_index:i + start_index]
                    # If current substring has been seen before, if it is a palindrome, increment ans.
                    if current_str in self.is_palindrome:
                        ans += 1
                    # If we have not seen substring before, check if it is a palindrome. 
                    else:
                        if self.check_palindrome(current_str):
                            ans += 1
        return ans
        
    def check_palindrome(self, word):
        """Check if the given word is a palindrome"""
        for i in range(len(word)//2):
            if word[i] == word[-i-1]:
                continue
            else:
                return False
        self.is_palindrome.add(word)
        return True
