def timeTarget (target:int, ps: tuple) -> float:
        return ((target-ps[0])/ps[1])
class Solution:
    

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(p,s,timeTarget(target, (p,s))) for p,s in zip(position, speed)]
        pairs.sort(reverse = True)
        stack = []
        for pair in pairs:
            stack.append(timeTarget(target, pair))
            if len(stack)>=2 and stack[-2]>=pair[-1]:
                stack.pop()
        return len(stack)

