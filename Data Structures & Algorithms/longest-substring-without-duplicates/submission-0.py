class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        answer=0
        seen=set()
        for right in range(0,len(s)):
            while s[right] in seen:
                seen.remove(s[left])      #remove from seen and increment left, as its a duplicate
                left=left+1
            seen.add(s[right])      #add new element
            answer=max(answer, right-left+1)
        return answer