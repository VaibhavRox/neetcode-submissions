class Solution:
    from collections import deque
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #use a deque
        dq=deque()
        result=[]
        for right in range(len(nums)):
            #drop from the back for smaller or equal values, useless now
            while dq and nums[dq[-1]]<=nums[right]:
                dq.pop()
            #add the new index
            dq.append(right)
            #drop from front
            if dq[0]<right-k+1: #checking if front slid out the window
                dq.popleft()
            
            #once window is full, checking
            if right>=k-1:
                result.append(nums[dq[0]])
        return result
