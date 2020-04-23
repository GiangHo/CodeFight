def reverseInParentheses(inputString):
    stack_str = []
    for i in inputString:
        if i != ")":
            stack_str.append(i)
        else:
            list_tmp = []
            while len(stack_str) != 0:
                character = stack_str.pop()
                if character != "(":
                    list_tmp.append(character)
                else:
                    stack_str += list_tmp
                    break
    return "".join(map(str, stack_str))
if __name__ == '__main__':
    reverseInParentheses("foo(bar(baz))blim")
