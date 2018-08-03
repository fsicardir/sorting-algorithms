
# Time complexity: O(n^2) in average case, O(n*log(n)) in best case
# Space complexity: O(1)
# Not stable

def comb_sort(arr):
    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]

    if len(arr) == 0: return

    gap = len(arr)
    swaps = 1

    while gap != 1 or (gap == 1 and swaps != 0):
        gap = int(gap / 1.3) if gap > 1 else gap
        if gap == 9 or gap == 10:
            gap = 11
        swaps = 0
        for i in range(len(arr) - gap):
            if arr[i] > arr[i + gap]:
                swap(i, i + gap)
                swaps += 1
