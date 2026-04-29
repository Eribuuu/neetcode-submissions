class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {}
        if len(s) != len(t):
            return False
            
        for letter in s:
            if letter not in count:
                count[letter] = 1
            else:
                count[letter] += 1
        
        for letter in t:
            if letter in count:
                count[letter] -= 1
        
        for letter in count:
            if count[letter] != 0:
                return False
        return True