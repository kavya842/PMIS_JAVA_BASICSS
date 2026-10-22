
class Solution:
    def twoSum(self, nums, target):
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
        return []
        
sol = Solution()
print("Test 1:", sol.twoSum([2,7,11,15], 9)) 
print("Test 2:", sol.twoSum([3,2,4], 6))       
print("Test 3:", sol.twoSum([3,3], 6))        