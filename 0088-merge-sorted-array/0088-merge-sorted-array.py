class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        x=nums1[:m]+nums2[:n]
        x.sort()
        nums1[:]=x
        return nums1

        
        