
# Time complexity: O(n^2), O(n) in best case
# Space complexity: O(1)
# Stable
def insertion_sort(arr):

    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]

    for i in range(1, len(arr)):
        j = i
        while arr[j] < arr[j - 1] and j > 0:
            swap(j, j -1)
            j-= 1

