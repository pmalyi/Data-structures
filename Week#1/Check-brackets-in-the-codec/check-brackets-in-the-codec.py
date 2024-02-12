def checkBrackets(str):
    stack = []
    for i in range(len(str)):
        if str[i] not in {'(', '[', '{', ')', ']', '}'} :
            continue
        else:
            if str[i] in {'(', '[', '{'}:
                stack.append((str[i], i + 1))
            else:
                if len(stack) == 0:
                    return i + 1  # Коли сама перша дужка закриваюча
                top = stack.pop()
                if top[0] == '(' and str[i] != ')' or \
                        top[0] == '[' and str[i] != ']' or \
                        top[0] == '{' and str[i] != '}':
                    return i + 1  # Номер першої закриваючої дужки для якої немає відкриваючої
    if len(stack) == 0:
        return 'Success'
    else:
        top = stack.pop()
        return top[1]   # Номер першої відкриваючої дужки для якої немає закриваючої


s = input()
print(checkBrackets(s))
