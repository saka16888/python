class Solution:
    def majorityElement(self, nums):
        m, count = None, 0
        for num in nums:
            if count == 0:
                m = num
            count += (1 if num == m else -1)
        return m

a=Solution()
nums=[7,1,5,3,6,4,1,5]
print(a.majorityElement(nums))