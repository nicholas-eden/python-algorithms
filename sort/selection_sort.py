from typing import List

data = [3, 6, 12, 6, 7, 4, 23, 7, 2, 1, 7, 4, 3, 2, 5, 3, 1]


def selection_sort(arr: List[int]):
    low: int
    for left in range(len(arr) - 1):
        low = left
        for right in range(left + 1, len(arr)):
            if arr[right] < arr[low]:
                low = right

        arr[left], arr[low] = arr[low], arr[left]


selection_sort(data)
print(data)
