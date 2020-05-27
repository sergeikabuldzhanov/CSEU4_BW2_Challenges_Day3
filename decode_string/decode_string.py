class Solution:
    def decodeString(self, s):
        # problem is similar to the "Balanced brackets" problem 
        # and thus can be solved the same way with some modifications
        stack = []
        for i in range(len(s)):
            # we are traversing the string looking for a closing bracket
            # once we've found it, we go back until we find an opening bracket
            # everythong between is a string to be multiplied by the number preceding the bracket
            if s[i] == "]":
                current = ''
                while stack:
                    val = stack.pop()
                    if val ==  "[":
                        break
                    current = val + current
                num = ''
                while stack and stack[-1].isdigit():
                    # this is getting the num after the opening bracket as a string
                    # since the num could be longer than a singl digit
                    num = stack.pop() + num
                stack.append(int(num)*current)
            else:
                stack.append(s[i])
        return ''.join(stack)