class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = []
        decode_dict = {
            '1':'a',
            '2':'b',
            '3':'c',
            '4':'d',
            '5':'e',
            '6':'f',
            '7':'g',
            '8':'h',
            '9':'i',
            '10':'j',
            '11':'k',
            '12':'l',
            '13':'m',
            '14':'n',
            '15':'o',
            '16':'p',
            '17':'q',
            '18':'r',
            '19':'s',
            '20':'t',
            '21':'u',
            '22':'v',
            '23':'w',
            '24':'x',
            '25':'y',
            '26':'z'
        }
        substring = []
        i = len(s) - 1
        # Walk backwards.  If the current char is a '#', use the previous 2 characters, otherwise use the given character.
        while i >= 0:
            curr_letter = s[i] 
            if curr_letter == '#':
                word = s[i-2:i]
                substring.append(decode_dict[word])
                i -= 3
            else:
                substring.append(decode_dict[s[i]])
                i -= 1
        substring = substring[::-1]
        return ''.join(substring)
