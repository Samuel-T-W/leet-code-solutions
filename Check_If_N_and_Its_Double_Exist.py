class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        s = set()
        for num in arr:
            if num*2 in s: return True
            if num%2 == 0 and int(num/2) in s: return True
            s.add(num)
        return False