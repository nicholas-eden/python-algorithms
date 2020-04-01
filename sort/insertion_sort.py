from typing import List

data = [3, 6, 12, 6, 7, 4, 23, 7, 2, 1, 7, 4, 3, 2, 5, 3, 1]


def insertion_sort(arr: List[int]):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


insertion_sort(data)
print(data)
