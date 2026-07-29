class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        def all_par(target):
            for i in range(len(nums1)):
                if (nums1[i] %2 == 0) == target:
                    continue
                found = False
                for j in range(len(nums1)):
                    diff =  nums1[i]-nums1[j]
                    if i == j:
                        continue
                    if (diff % 2 == 0) == target:
                         found = True
                         break
                if not found:
                    return False
            return True
        return all_par(False) or all_par(True)
        
                
        
        # nums2=[nums1[0]]*len(nums1)
        # if nums1[0] % 2 == 0:
        #     for i in range(1, len(nums1)):
        #         if nums1[i] % 2 == 0:
        #             nums2[i]=nums1[i]
        #         else:
        #             found = False
        #             for j in range(i):
        #                 diff = nums1[i]-nums1[j]
        #                 if diff % 2 ==0:
        #                     nums2[i]=diff
        #                     found = True
        #                     break
        #             if not found:
        #                 return False
                    
        # else:
        #     for i in range(1, len(nums1)):
        #         if nums1[i] % 2 != 0:
        #             nums2[i]=nums1[i]
        #         else:
        #             found = False
        #             for j in range(i):
        #                 diff = nums1[i]-nums1[j]
        #                 if diff % 2 !=0:
        #                     nums2[i]=diff
        #                     found = True
        #                     break
        #             if not found:
        #                 return False
        # return True
        