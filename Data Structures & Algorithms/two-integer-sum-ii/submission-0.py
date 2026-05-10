class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i1 = 0
        i2 = len(numbers) - 1

        while (i1 != i2):
            sum = numbers[i1] + numbers[i2] 

            if (sum > target):
                i2 -= 1
            elif (sum < target):
                i1 += 1    
            else:
                return [i1 + 1, i2 + 1] 
        return []