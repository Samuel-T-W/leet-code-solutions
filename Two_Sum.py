class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
            dct={}
            for i in range(len(nums)):
                dct.update({nums[i] : i})
                
            
            for i in range(len(nums)):
                x= target-nums[i]
                if(dct.get(x)):
                    if(dct.get(x)!=i):
                        return [i, dct.get(x)]
                    