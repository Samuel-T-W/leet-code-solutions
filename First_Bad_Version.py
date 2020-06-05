class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        x=n
        top=n
        bot=1
        ex=True
        
        while(ex):
            val = isBadVersion(x)

            if(val==True):
                top=x
                if(top<=bot):
                    ex=False
                x=((top+bot)//2)
            else:
                bot=x+1
                if(top<=bot):
                    ex=False
                x=((top+bot)//2)
            
        return x