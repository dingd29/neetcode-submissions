class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        candict = {')':'(', '}': '{', ']': '['}
        for char in s:
            if char in candict.values():
                stack.append(char)
            else: 
                if not stack or stack[-1] != candict[char]:
                    return False
                stack.pop()
        return not stack