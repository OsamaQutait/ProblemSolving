def groupAnagrams(strs):
    str2 = []
    dictionary = {}
    strs1 = []
    for s in strs:
        s = "".join(sorted(s))
        strs1.append(s)
    for i in range(len(strs1)):
        if strs1[i] not in dictionary:
            dictionary[strs1[i]] = strs(i)
        else:
            list(dictionary[strs1[i]]) + list([strs(i)])
    for s in dictionary:
        str2.append(dictionary[s])
    return str2
if __name__ == '__main__':
    print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))



