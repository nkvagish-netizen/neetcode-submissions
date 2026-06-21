class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq=deque()
        result=[]
        left=0
        for right in range(len(nums)):
            
            while dq and nums[dq[-1]] < nums[right]:        # Remove smaller elements
                dq.pop()
            dq.append(right)
            if dq[0] < left:                                # Remove out-of-window indices
                dq.popleft()
            if right+1 >= k:                                 # Window formed
                result.append(nums[dq[0]])
                left+=1
        return result