class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        
        for i in range(len(nums)):
            num = 1
            for j in range(len(nums)):
                if (i != j):
                    num *= nums[j]
            res[i] = num
        
        return res