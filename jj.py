def isValid(s):
    characters = {")": "(",
                  "}": "{",
                  "]": "["}
    stack = []
    for i in s:
        if i in characters:
            if stack and stack[-1] == characters[i]:
                stack.pop()
            else:
                return False
        else:
            stack.append(i)
    return True if not stack else False

if __name__ == '__main__':
    print(isValid("()[]{}{{"))

