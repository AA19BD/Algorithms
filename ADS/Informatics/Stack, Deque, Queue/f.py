def isValid(s: str) -> bool:
    stack = []
    for i in range(len(s)):
        if (s[i] == '(' or s[i] == '[' or s[i] == '{'):
            stack.append(s[i])
        else:
            if len(stack) == 0:
                return False
            top = stack[-1]
            if (top == '(' and s[i] != ')'):
                return False
            if (top == '[' and s[i] != ']'):
                return False
            if (top == '{' and s[i] != '}'):
                return False
            stack.pop()

    return not stack

n = input()
if isValid(n):
    print('yes')
else:
    print('no')