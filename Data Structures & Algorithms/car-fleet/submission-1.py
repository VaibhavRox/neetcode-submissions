class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #can also just use a ahead_time var, not necessary to use stack,
        cars=sorted(zip(position,speed),reverse=True)
        ahead_time=0
        fleets=0
        #same conditioning and all, instead of appending, increment fleets, and instead of appending to stack, just update the ahead_time
        for pos,s in cars:
            behind_time=(target-pos)/s
            if behind_time>ahead_time: #behind car will take more time to reach target, thus wont ever merge to ahead car, new fleets
                fleets+=1
                ahead_time=behind_time
        return fleets