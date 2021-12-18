import collections
nums = [1, 0, 5, 1, -1, 2]
freq = collections.Counter(nums)
print(freq)
print(sorted(set(nums)))
res = []
target = 2
l = 0
for i in range(len(nums)-2):
    for j in range(i+1, len(nums)):
        1
