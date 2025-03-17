class Solution(object):
    def jump(self, nums):
        \\\
        :type nums: List[int]
        :rtype: int
        \\\
        n=len(nums)
        if n==1:
            return 0
        endOfCurrentJump=0
        maxReach=0
        jump=0

        for i in range(n-1):
            maxReach = max(maxReach, i+ nums[i])

            if i == endOfCurrentJump:
                jump+=1
                endOfCurrentJump= maxReach

            if endOfCurrentJump >= n-1:
                break

        return jump