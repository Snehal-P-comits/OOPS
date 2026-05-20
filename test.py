numlist = [1, 1, 2, 2, 3, 3, 4]

'''
the time complexity of this code is O(n^2) because we have two nested loops

n = len(numlist)
unique = None

for i in range(n):
    count = 0
    for j in range(n):
        if numlist[i] == numlist[j]:
            count += 1
    if count == 1:
        unique = numlist[i]
        break

print(unique)
'''

'''the time complexity of this code is O(n) because we have a single loop that iterates through the list once and that's it'''
def find_unique(numlist):
    result = 0

    for num in numlist:
        result ^= num   # ^= is XOR operation

    return result



print(find_unique(numlist))