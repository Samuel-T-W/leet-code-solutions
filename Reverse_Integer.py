class Solution:
    def reverse(self, x: int) -> int:
        
        n = str(x)
        r=""
        if (n[0]=="-"):
            r += "-" 
            n = n[1:]
            c = int(r + n[::-1])
            if(-(2**31)<=c<=(2**31 -1)):
                return c
            else:
                return 0
        y = int(n[::-1])
        if(-(2**31)<=y<=(2**31 -1)):
            return y
        else:
            return 0