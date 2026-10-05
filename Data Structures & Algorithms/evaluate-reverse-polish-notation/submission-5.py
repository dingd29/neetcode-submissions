import operator
class Solution:
   
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {'+': operator.add,'-': operator.sub,'*': operator.mul,'/': lambda a,b: int(a/b)}
        for char in tokens:
            if char.strip('-').isdigit():
                if '-' in char:
                    stack.append(int(char))
                else:
                    stack.append(int(char))
            else:
                b=stack.pop()
                a=stack.pop()
                stack.append(operations[char](a,b))
        return stack.pop()
