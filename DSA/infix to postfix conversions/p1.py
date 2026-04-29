def conversion(n):
    stack=[]
    result=""
    for i in n:
        if i.isalnum():
            result+=i
        elif i=='(':
            stack.append(i)
        elif i==')':
            while stack[-1]!='(':
                result+=stack.pop()
            stack.pop()
        else:
            while(stack and stack[-1]!='(' and
                   (i in "+-" and stack[-1] in "+-*/" or
                    i in "*/" and stack[-1] in "*/")):
                result += stack.pop()
            stack.append(i)
    while stack:
        result+=stack.pop()
    return result
n="A+B*(C-D)"
print(conversion(n))
