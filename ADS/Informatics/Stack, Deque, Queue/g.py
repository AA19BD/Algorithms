def Postfix_notation(s:str) -> list[int]:

    stack = []
    for i in s.split():
        if i != '+' and i != '-' and i != '*' :
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

    return stack

a = input()
print(Postfix_notation(a))



