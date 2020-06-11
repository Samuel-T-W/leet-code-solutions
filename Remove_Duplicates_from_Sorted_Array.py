class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if(len(nums)>0):
            past=nums[0]
            c= 1
        else:
            return 0
        
        for i in nums:
            if(past != i):
                nums[c] = i
                c +=1
                past = i
        return c