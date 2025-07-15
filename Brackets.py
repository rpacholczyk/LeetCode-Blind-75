class Solution:
    def isValid(self, s: str) -> bool:
        # A stack that stores the brackets
       stack = []
       for item in range(len(s)):
        # Confirm that the item is an opening bracket
        if s[item] == '(' or s[item] == '{' or s[item] == '[':
            stack.append(s[item])
        else:
            # If it's a closing bracket, check if the stack is non-empty
            # and if the top of the stack is a matching opening bracket
            if stack and (
                (stack[-1] == '(' and s[item] == ')') or
                (stack[-1] == '{' and s[item] == '}') or
                (stack[-1] == '[' and s[item] == ']')):
                # Pop the matching opening bracket
                stack.pop()
            else:
                # Unmatched closing bracket
                return False
     # If stack is empty, return True (balanced), otherwise False
       return not stack
