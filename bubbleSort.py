
# Time complexity: O(n^2) in average case
# Space complexity: O(1)
# Stable

def bubble_sort(arr):
    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]

    j = len(arr) - 1
    while j > 0:
        for i in range(j):
            if arr[i] > arr[i + 1]:
                swap(i, i + 1)
            i += 1

        j -= 1
