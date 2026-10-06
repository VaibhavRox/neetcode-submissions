class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        answer=0
        max_count=0
        char_freq=[0]*26   #to count the occurences of the character
        for right in range(len(s)):

            # add the count
            char_freq[ord(s[right])-ord('A')]+=1
            max_count=max(max_count,char_freq[ord(s[right])-ord('A')]) #update max_count if current char count is higher
            while (right-left+1)-max_count>k:   #if number of replacements is more than k(max replacement chars)
                char_freq[ord(s[left])-ord('A')]-=1
                left+=1
            answer=max(answer,right-left+1)
        return answer

