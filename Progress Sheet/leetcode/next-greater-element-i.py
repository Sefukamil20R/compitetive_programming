class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dis = defaultdict(int)
        stack = []
        res = [-1]*len(nums1)
        for i in range (len(nums1)):
              dis[nums1[i]] = i 
        for i in range(len(nums2)):
            current = nums2[i]
            while stack and current > stack[-1]:
                     elem = stack.pop()
                     res[dis[elem]] = current
            if nums2[i] in dis:
                stack.append(nums2[i])
        return res 
        
        