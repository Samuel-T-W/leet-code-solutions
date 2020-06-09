class Solution:       
    def romanToInt(self, s: str) -> int:
        dic = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
        }   
        m=[]
        r=0
        
        
        for i,c  in enumerate(s):
            m.append(c)
            if (len(m) == 2):
                if(dic.get(m[0]) >= dic.get(m[1])):
                    r += dic.get(m.pop(0))
                    continue
                if(dic.get(m[1]) > dic.get(m[0])):
                    r += (dic.get(m.pop(1)) - dic.get(m.pop(0)))
                    
                    
        if (len(m)>0):
            r+= dic.get(m[0])
            
        return r