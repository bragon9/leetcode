class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        secret_dict = {str(i):0 for i in range(10)}
        guess_dict = {str(i):0 for i in range(10)}
        bulls = 0
        cows = 0
        print(secret_dict)
        for i in range(len(secret)):
            s_char = secret[i]
            g_char = guess[i]
            if s_char == g_char:
                bulls += 1
            else:
                secret_dict[s_char] += 1
                guess_dict[g_char] += 1
        for i in range(10):
            cows += min(secret_dict[str(i)], guess_dict[str(i)])
        return f'{bulls}A{cows}B'
