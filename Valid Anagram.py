def isAnagram(s, t):
    s = sorted(s)
    t = sorted(t)
    s = "".join(s)
    t = "".join(t)
    if s == t:
        return True
    else:
        return False


if __name__ == '__main__':
    print(isAnagram("cat", "tar"))
