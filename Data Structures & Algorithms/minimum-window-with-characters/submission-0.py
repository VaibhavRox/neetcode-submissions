class Solution:
    from collections import Counter

    def minWindow(self, s: str, t: str) -> str:
        # create a counter dict for t_freq, then another window_freq
        # use a need/have var, valid only when need==have
        if len(t) > len(s):
            return ""
        t_freq = Counter(t)
        window_freq = Counter()
        need = len(set(t))  # to get distinct letters in t
        have = 0
        left = 0
        best_length = float("inf")
        best_left = 0
        for right in range(len(s)):
            c = s[right]
            window_freq[c] = window_freq.get(c, 0) + 1
            # add only when c in t_freq letters
            if c in t_freq and window_freq[c] == t_freq[c]:
                have += 1
            while have==need:
                #update if best_length
                if right-left+1<best_length:
                    best_length=right-left+1
                    best_left=left
                #if not , remove left character and its counter
                if s[left] in t_freq and window_freq[s[left]]==t_freq[s[left]]:
                    have-=1
                window_freq[s[left]]-=1
                left+=1

        if best_length==float('inf'):
            return ""
        return s[best_left:best_length+best_left]
