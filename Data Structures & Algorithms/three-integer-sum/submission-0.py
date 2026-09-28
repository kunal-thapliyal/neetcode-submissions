class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        lst = []
        nums.sort()

        for k in range (n-2): 
            if k > 0 and nums[k] == nums[k-1]:
                continue
            
            left = k +1
            right = n - 1
            sum = -1 * nums[k]

            while left < right: 
                s = nums[left] + nums[right]

                if sum > s: 
                    left += 1 
                elif sum < s: 
                    right -= 1
                else: 
                    lst.append([nums[k],nums[left],nums[right]])
                    left += 1 
                    right -= 1

                    while left < n and nums[left] == nums[left-1]:
                        left+= 1
                    while right <= 0 and nums[right] == nums[right+1]: 
                        right-=1
        return lst




