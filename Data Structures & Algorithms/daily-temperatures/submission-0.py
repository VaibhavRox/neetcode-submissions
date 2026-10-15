class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #use indices in a stack to get the number of days 
        # in stack store indices to hold the current top element as the tempretaure
        n=len(temperatures)
        result=[0]*n
        stack=[]
        for i in range(n):
            while stack and temperatures[i]>temperatures[stack[-1]]:  #if today is warmer than previously seen day index in stack top
                prev=stack.pop()
                result[prev]=i-prev #the diff in number of days
            stack.append(i)
        return result