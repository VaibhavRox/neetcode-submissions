class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        char_freq=[0]*26
        for i in s:
            char_freq[ord(i)-ord('a')]+=1
        for i in t:
            char_freq[ord(i)-ord('a')]-=1
        if not any(char_freq):  #any checks the truthy value, if all freq zero then it returns false, flip it and you have the answer
            return True
        else:
            return False