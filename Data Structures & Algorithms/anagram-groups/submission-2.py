class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana={}
        for i in strs:
            char_freq=[0]*26
            for j in i:
                char_freq[ord(j)-ord('a')]+=1
            key=tuple(char_freq)
            if key in ana:
                ana[key].append(i)
            else:
                ana[key]=[i]
        return list(ana.values())