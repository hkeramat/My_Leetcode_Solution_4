class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        m = len(nums1)
        n = len(nums2)
        i = 0
        j = 0
        k = 0
        merged_arr = [0] * (m+n)
        while i < m and j < n:
            
            
            next_1 =nums1[i]
            next_2 = nums2[j]
                
            if next_1 <= next_2:
                merged_arr[k] = next_1
                i +=1
            elif next_1 > next_2:
                merged_arr[k] =  next_2
                j+=1
            k+=1

        if j < n:
            merged_arr[k:] = nums2[j:]
        elif i < m:
            merged_arr[k:] = nums1[i:]
            
        
        if (m+n)%2 == 0:
            Median = (merged_arr[(m+n)//2 -1] +merged_arr[(m+n)//2 ])/2
            
        else:
            Median = merged_arr[(m+n)//2]
        
        return Median
