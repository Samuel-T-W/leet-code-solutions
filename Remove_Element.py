class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count=[]
        y= nums.count(val)
        for i in range(y):
            nums.remove(val)
        return len(nums)
        