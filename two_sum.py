# The following code adds two numbers and returns thre index of the two numbers
# The two numbers are added and the sum is compared to the target

class Solution:

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        listNum = []
        for i, value in enumerate(nums):  # 1
            remaining = target - nums[i]  # 2
            listNum.append(value)

            if remaining in seen:  # 3
                return [i, seen[remaining]]  # 4
            else:
                seen[value] = i  # 5


# Creating an objec of the class solution and calling the twoSum method
so = Solution()
print(so.twoSum([2, 7, 11, 15], 9))

