nums = [2, 7, 11, 15]
target = 9
size = len(nums)

for i in range(size):
    for j in range(i + 1, size):  # avoid repeating pairs and self-pairs
        if nums[i] + nums[j] == target:
            print(i, j)


