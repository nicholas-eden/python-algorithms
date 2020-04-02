from typing import List


def remove_duplicates_in_sorted_list(self, nums: List[int]) -> int:
    if len(nums) == 0:
        return 0

    cur = 1
    for i in range(1, len(nums)):
        if nums[i - 1] == nums[i]:
            continue
        nums[cur] = nums[i]
        cur += 1

    del nums[cur:]