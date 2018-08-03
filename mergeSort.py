
# Time complexity: O(n*log(n))
# Space complexity: O(n)
# Stable
def merge_sort(arr):

    def merge(list1, list2):
        i, j = 0, 0
        merge = []
        while i < len(list1) and j < len(list2):
            if list1[i] > list2[j]:
                merge.append(list2[j])
                j += 1
            else:
                merge.append(list1[i])
                i += 1
        merge += list1[i:]
        merge += list2[j:]
        return merge

    if len(arr) < 2:
        return arr
    half = len(arr) // 2
    left = merge_sort(arr[:half])
    right = merge_sort(arr[half:])
    return merge(left, right)

