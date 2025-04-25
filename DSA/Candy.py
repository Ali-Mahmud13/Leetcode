class Solution(object):
    def candy(self, ratings):
        \\\
        :type ratings: List[int]
        :rtype: int
        \\\
        n=len(ratings)
        sum=0
        assigned_candy=[1]*n
        for i in range(1,n):
            if ratings[i]>ratings[i-1]:
                assigned_candy[i]=assigned_candy[i-1]+1
        for i in range(n-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                assigned_candy[i]=max(assigned_candy[i],assigned_candy[i+1]+1)
        
        for i in range(n):
            sum+=assigned_candy[i]
        return sum