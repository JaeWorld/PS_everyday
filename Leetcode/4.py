# Leetcode 3. Median of Two Sorted Arrays

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        temp = []
        res = 0
        
        i1, i2 = 0, 0
        
        if m == 0:
            if n%2 == 1:
                return nums2[n//2]
            else:
                return (nums2[n//2] + nums2[n//2-1])/2
        elif n == 0:
            if m%2 == 1:
                return nums1[m//2]
            else:
                return (nums1[m//2] + nums1[m//2-1])/2
        
        while True:
            if nums1[i1] >= nums2[i2]:
                temp.append(nums2[i2])
                if i2+1 < n:
                    i2 += 1
                else:
                    temp.extend(nums1[i1:])
            elif nums1[i1] < nums2[i2]:
                temp.append(nums1[i1])
                if i1+1 < m:
                    i1 += 1
                else:
                    temp.extend(nums2[i2:])
                    
            if len(temp) == m+n:
                if (m+n)%2 == 1:
                    res = temp[len(temp)//2]
                else:
                    res = (temp[len(temp)//2] + temp[len(temp)//2-1]) / 2
                break
                
        return res
