class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #method, build s1_freq array first, then in the loop build a window_freq that grows with sliding window, and check it with s1_freq
        m=len(s1)
        n=len(s2)
        if m>n:
            return False #obviously if s1>s2, how you gonna check
        s1_freq=[0]*26
        for c in s1:
            s1_freq[ord(c)-ord('a')]+=1
        window_freq=[0]*26
        left=0
        for right in range(n):
            window_freq[ord(s2[right])-ord('a')]+=1
            if right-left+1 == m:       #window full
                if s1_freq==window_freq:
                    return True
                window_freq[ord(s2[left])-ord('a')]-=1  #left index is moving
                left+=1
        return False
