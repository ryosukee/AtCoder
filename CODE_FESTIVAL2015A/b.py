length = int(input())
nums = input().split()

total = 0
for i in range(length):
    total += int(nums[i]) * (2 ** (length-1-i))
print(total)
