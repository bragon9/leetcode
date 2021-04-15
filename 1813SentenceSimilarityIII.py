class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        def check_front(short, long):
            '''Walk from the front of each sentence as long as they are the same word.
            Return the words leftover once there is a difference'''
            for i in range(len(short)):
                if short[i] != long[i]:
                    return short[i:]
                
        def check_back(short, long):
            '''Walk backwards as long as each sentence has the same word.
            If they all match, return True.'''
            if not(short):
                return True
            diff = len(long) - len(short)
            for i in range(len(short)-1,-1,-1):
                if short[i] != long[i+diff]:
                    return False
            return True
            
        if not(sentence1) or not(sentence2):
            return True
        # Break each sentence into words
        s1 = sentence1.split()
        s2 = sentence2.split()
        if s1 == s2:
            return True
        elif len(s1) == len(s2):
            return False
        # Set the short/long sentences.
        if len(s1) > len(s2):
            short = s2
            long = s1
        else:
            short = s1
            long = s2
        # Check validity
        remainder = check_front(short, long)
        return check_back(remainder, long)
            
        
        
        
       
                    
        
