def Postfix_notation(s:str) -> int:

    stack = []
    for i in s.split():
        if i not in '+-*':
            stack.append(i)
        else:
            if i == '+':
                top = stack.pop()
                bottom = stack.pop()
                stack.append(int(top)+int(bottom))
            elif i == '-':
                top = stack.pop()
                bottom = stack.pop()
                stack.append(int(bottom)-int(top))
            elif  i == '*':
                top = stack.pop()
                bottom = stack.pop()
                stack.append(int(top)*int(bottom))


    return stack[-1]

a = input()
print(Postfix_notation(a))



