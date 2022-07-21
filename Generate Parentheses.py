def generateParenthesis(n):
    stack = []
    arr = []
    #
    #
    #

#
#
#

    def backTrack(open, close):
        if open == close == n:
            arr.append("".join(stack))
            return
        if open < n:
            stack.append("(")
            backTrack(open+1, close)
            stack.pop()
        if close < open:
            stack.append(")")
            backTrack(open, close+1)
            stack.pop()
    backTrack(0, 0)
    return arr


print(generateParenthesis(2))




