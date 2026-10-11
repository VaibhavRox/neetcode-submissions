class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2==1:
            return False  #odd length
        pairs={')':'(',']':'[','}':'{'} #creating pair dict for brackets
        stack=[]
        for c in s:
            if c in pairs:
                if stack and stack[-1]==pairs[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)   #add element to stack
        return not stack  #check if stack is empty by the end