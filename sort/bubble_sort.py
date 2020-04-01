from typing import List

data = [3, 6, 12, 6, 7, 4, 23, 7, 2, 1, 7, 4, 3, 2, 5, 3, 1]


def bubble_sort(arr: List[int]):
    swap = True
    partition = len(arr)
    while swap:
        swap = False
        for i in range(partition - 1):
            if arr[i] > arr[i + 1]:
                swap = True
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

        partition -= 1


bubble_sort(data)
print(data)
