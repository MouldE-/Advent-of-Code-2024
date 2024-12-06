with open("day1-input", "r") as file:
    nums = [int(num) for num in file.read().split()]
l1, l2 = nums[0:len(nums):2], nums[1:len(nums):2]
l1.sort()
l2.sort()
print(sum([abs(item1 - item2) for item1, item2 in zip(l1, l2)]))
