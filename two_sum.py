from utils import test

def twoSum(nums, target):
    checked = {}
    for i in range(len(nums)):
        num = nums[i]
        if target - num in checked:
            return (i, checked[target - num])
        checked[num] = i

tests = list(range(1, 1000))
print(twoSum(tests, 195))


