def containsDuplicate(nums):
    dictionary = {}
    for num in nums:
        if num in dictionary:
            return True
        else:
            dictionary[num] = True
    return False
"""
dictionary = {}
for num in nums:
    dictionary[num] = False
if len(dictionary) == len(nums):
    return False
else:
    return True
"""
if __name__ == '__main__':
    print(containsDuplicate([1, 2, 3, 1]))


