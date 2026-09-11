class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        temp=sorted(set(arr))
        d={}
        for i,num in enumerate(temp,start=1):
            d[num]=i
        return[d[num]for num in arr]