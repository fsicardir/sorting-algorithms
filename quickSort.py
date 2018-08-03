
# Time complexity: O(n*log(n))
# Space complexity: O(n)
# Not stable
def quick_sort(arr):
    if len(arr) < 2: return arr

    pivot = arr[0]
    less, equal, more = [], [], []
    for element in arr:
        if element > pivot:
            more.append(element)
        elif element == pivot:
            equal.append(element)
        else:
            less.append(element)

    return quick_sort(less) + equal + quick_sort(more)


# Time complexity: O(n*log(n))
# Space complexity: O(1)
# Not stable
def inplace_quick_sort(arr):

    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]

    def partition(fi, li):
        i = j = fi + 1
        while j <= li:
            if arr[j] <= arr[fi]:
                swap(j, i)
                i += 1
            j += 1
        swap(fi, i - 1)
        return i - 1

    def sort(fi, li):
        if li - fi < 1: return
        pivotIdx = partition(fi, li)
        sort(fi, pivotIdx - 1)
        sort(pivotIdx + 1, li)

    sort(0, len(arr) - 1)
