
# Time complexity: O(n^2)
# Space complexity: O(1)
# Not stable
def selection_sort(arr):

    def find_max(lst):
        max = 0
        for i in range(1,lst + 1):
            max = i if (arr[i] > arr[max]) else max
        return max

    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]

    for i in range(len(arr) - 1, 0, -1):
        swap(find_max(i), i)
