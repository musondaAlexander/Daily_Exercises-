# The following code adds two numbers and returns thre index of the two numbers
# The two numbers are added and the sum is compared to the target

class Solution:
   def twoSum(self, nums: list[int], target: int) -> list[int]:
       seen = {}
       for i, value in enumerate(nums): #1
           remaining = target - nums[i] #2
           
           if remaining in seen: #3
               return [i, seen[remaining]]  #4
           else:
               seen[value] = i  #5