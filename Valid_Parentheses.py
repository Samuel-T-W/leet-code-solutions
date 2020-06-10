class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        if (len(s) % 2 != 0):
            return False
        
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
        
            else:
                if not stack:
                    return False
                b=stack.pop()
                if b == '(' and s[i] != ')':
                    return False
                if b == '{' and s[i] != '}':
                    return False
                if b == '[' and s[i] != ']':
                    return False
        if stack:
            return False
        return True