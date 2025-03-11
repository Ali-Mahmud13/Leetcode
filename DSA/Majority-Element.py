class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        candidate=None

        for i in range(0,len(nums)):
            if count==0:
                candidate=nums[i]
            if nums[i]== candidate:
                count+=1
            else:
                count-=1
        return candidate
        
