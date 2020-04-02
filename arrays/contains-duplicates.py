from typing import List


def contains_duplicate(self, nums: List[int]) -> bool:
    unique = set(nums)
    return len(unique) != len(nums)