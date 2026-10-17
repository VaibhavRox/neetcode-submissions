class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars=sorted(zip(position,speed),reverse=True)   #sorted by position
        stack=[]
        for pos,s in cars:
            time_behind=(target-pos)/s
            if not stack or time_behind>stack[-1]:      #basically if time taken by car behind is more, then it wont catch up and make a new fleet
                stack.append(time_behind)
        return len(stack)