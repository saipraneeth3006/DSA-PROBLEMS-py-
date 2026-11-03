class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        sum=0
        l=nums1+nums2
        l=sorted(l)
        if len(l)%2==0:
            sum=(l[len(l)//2]+l[(len(l)//2)-1])/2
        else:
            sum=l[len(l)//2]
        return sum
        