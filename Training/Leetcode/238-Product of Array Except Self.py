class Solution:
    def productExceptSelf(self,nums):
        '''
        :param nums:
        :return: array answer
        nums[i]: (nums[0]*...nums[i-1])*(nums[i+1]*..*nums[n-1])
        '''
        n = len(nums)
        answer = [1] * n

        # Calculate prefix products
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]
        print("nums",nums, "Prefix answer",answer)

        # Calculate suffix products and combine with prefix products
        suffix = 1
        for i in range(n - 1, -1, -1):
            print(i,suffix)
            answer[i] *= suffix
            suffix *= nums[i]
        print("answer",answer)
        return answer

a=Solution()
nums=[1,2,3,4]
a.productExceptSelf(nums)
#print(a.productExceptSelf(nums))

nums=[-1,1,0,-3,3]
print(a.productExceptSelf(nums))

