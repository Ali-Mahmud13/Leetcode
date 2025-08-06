class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        r=""
        # d={
        #     1:'I',
        #     4:'IV',
        #     5:'V',
        #     9:'IX',
        #     10:'X',
        #     40:'XL',
        #     50:'L',
        #     90:"XC",
        #     100:'C',
        #     400:'CD',
        #     500:'D',
        #     900:'CM',
        #     1000:'M'

        # }
        
        for i in range(num/1000):
            r+='M'
            num-=1000

        if num/900==1:
            r+='CM'
            num-=900
        else:
            D=num/500
            num=num%500
            for i in range(D):
                r+='D'
        
        C=num/100
        num=num%100
        if C==4:
            r+='CD'
       
        else: 
            for i in range(C):
                r+='C'

        if num/90==1:
            r+='XC'
            num-=90
        else:
            L=num/50
            num=num%50

            for i in range(L):
                r+='L'

        X=num/10
        num=num%10
        if X==4:
            r+='XL'
        
        else: 
            for i in range(X):
                r+='X'

        if num==9: 
            r+='IX'
            num-=9
        else:
            V= num/5
            num=num%5
            for i in range(V):
                r+='V'
        
        
        if num==4:
            r+='IV'
        
        else: 
            for i in range(num):
                r+='I'

        return r


        



        



            
                

            