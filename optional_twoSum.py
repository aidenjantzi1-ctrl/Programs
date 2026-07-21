"""
Given a 1-based indexed integer array arr[] that is sorted in non-decreasing order, along with an integer target. find two elements in the array such that their sum is equal to target. If such a pair exists, return the indices of the two elements in increasing order. If no such pair exists, return [-1, -1].

Examples:

Input: arr[] = [2, 7, 11, 15], target = 9
Output: 1 2
Explanation: Since the array is 1-indexed, arr[1] + arr[2] = 2 + 7 =  9

Input: arr[] = [1, 3, 4, 6, 8, 11] target = 10
Output: 3 4
Explanation: Since the array is 1-indexed, arr[3] + arr[5] = 4 + 6 = 10
"""

def two_sum_hash(arr: list, target: int) -> list:
    checked = {}
    for i in range(len(arr)):
        num = arr[i]
        if target - num in checked:
            currentIndex = i + 1
            complementIndex = checked[target - num] + 1
            if currentIndex > complementIndex:
                return [complementIndex, currentIndex]
            else:
                return [currentIndex, complementIndex]
            
        checked[num] = i
    return [-1, -1]


def two_sum_pointers(arr: list, target: int) -> list:
    leftIndex = 0
    rightIndex = len(arr) - 1
    while leftIndex < rightIndex:
        twoSum = arr[leftIndex] + arr[rightIndex]
        if twoSum == target:
            return [leftIndex + 1, rightIndex + 1]
        elif twoSum < target:
            leftIndex += 1
        else:
            rightIndex -= 1
    return [-1, -1]

if __name__ == "__main__":
    example_arr = list(range(1, 100000))
    example_target = 1999854
    print(f"arr={example_arr}, target={example_target}\n")

    print("Hash Map:")
    output = two_sum_hash(example_arr, example_target)
    print(f"Output: {output}\n")

    print("Two Pointer:")
    output = two_sum_pointers(example_arr, example_target)
    print(f"Output: {output}")
