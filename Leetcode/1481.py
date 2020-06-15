class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        dic = {}
        removed = 0
        n = len(arr)
        for i in range(n):
            if arr[i] in dic:
                dic[arr[i]] += 1
            else:
                dic[arr[i]] = 1
                
        dic = sorted(dic.items(), key=lambda x: x[1])
        
        for i in range(len(dic)):
            k -= dic[i][1]
            if k >= 0:
                removed += 1
            else:
                break
                
        return len(dic)-removed
