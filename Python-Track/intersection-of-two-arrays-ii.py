class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        for i in range (len(nums1)):
            if nums1[i] in nums2:
                 ans.append(nums1[i])
                 nums2.remove(nums1[i])
        return ans
        # count1=Counter(nums1)
        # count2=Counter(nums2)
        # print(count1)
        # print(count2)
        # ans=[]
        # for i in range (len(nums1)):
        #     if nums1[i] in count1 and nums1[i] in count2:
        #         ans.extend([nums1[i]]*(min(count1[nums1[i]],count2[nums1[i]])))
        # return ans 
        