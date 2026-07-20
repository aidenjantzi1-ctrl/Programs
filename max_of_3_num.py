
def maxOfThree(nums):
    highest = nums[0]
    for num in nums:
        if num > highest:
            highest = num
    return highest

# output: 15
print(max(3, 15, 9))