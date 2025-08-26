class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        n=len(numbers)
        j=n-1
        output=[]
        k=0
        for i in range(n):
            if numbers[k]+numbers[j]>target:
                j-=1
            elif numbers[k]+numbers[j]<target:
                k+=1
            else:
                output.append(k+1)
                output.append(j+1)

                return output
            
            
        