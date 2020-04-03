from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []

        if len(nums) == 1:
            return [nums]

        perms = []

        for i in range(len(nums)):
            m = nums[i]
            rem = nums[:i] + nums[i+1:]

            for p in self.permute(rem):
                perms.append([m] + p)

        return perms


test = Solution()
result = test.permute([1, 2, 3])
print(result)
