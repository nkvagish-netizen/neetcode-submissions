class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left=0
        right=len(numbers)-1
        while left < right:
            nums = numbers[left]+numbers[right]
            if nums == target:
                return [left+1 , right+1]
            elif nums < target:
                left+=1
            else:
                right-=1
