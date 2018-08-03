from sorting.countingSort import counting_sort_for_radix


# Time complexity: O(n)
# Space complexity: O(1)
# Stable
def radix_sort(arr, digits):
    mod = 10
    for i in range(digits):
        counting_sort_for_radix(arr, 9, lambda x: ((x % mod) // (mod // 10)))
        mod *= 10
