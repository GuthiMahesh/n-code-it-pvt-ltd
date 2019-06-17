# Python3 Program to Create list
# with integers within given range

def checkConsecutive(l):
    return sorted(l) == list(range(min(l), max(l) + 1))


# Driver Code
lst = [2, 3, 1, 4, 5]
print(checkConsecutive(lst))
