class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        li=[]
        if len(nums1)>=len(nums2):
            for i in nums1:   
                if i in nums2:
                    li.append(i)
                    nums2.remove(i)
            return li
        elif len(nums2)>len(nums1):
            for i in nums2:   
                if i in nums1:
                    li.append(i)
                    nums1.remove(i)
            return li
            
        