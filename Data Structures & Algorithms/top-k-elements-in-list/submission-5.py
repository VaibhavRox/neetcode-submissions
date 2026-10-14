class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        count=Counter(nums)
        ordered=sorted(count.items(),key=lambda pair:pair[1],reverse=True)
        return [i[0] for i in ordered[:k]]
        
        
            