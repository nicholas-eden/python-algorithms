from typing import List

data = [3, 6, 12, 6, 7, 4, 23, 7, 2, 1, 7, 4, 3, 2, 5, 3, 1]


def merge_sort(arr: List[int]) -> List[int]:
    return sort(arr)


def sort(arr: List[int]) -> List[int]:
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    return merge(sort(arr[0: mid]), sort(arr[mid:]))


def merge(a: List[int], b: List[int]) -> List[int]:
    merged: List[int] = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1

    merged.extend(a[i:])
    merged.extend(b[j:])

    return merged


data = merge_sort(data)
print(data)
