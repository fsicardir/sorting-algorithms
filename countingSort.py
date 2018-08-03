from collections import deque

# Time complexity: O(n+k)
# Space complexity: O(k)
# Stable
def counting_sort(arr, k):
    k += 1
    aux = [0 for _ in range(k)]
    for i in arr:
        aux[i] += 1
    i = 0
    for j in range(k):
        for l in range(aux[j]):
            arr[i] = j
            i += 1

# Time complexity: O(n+k)
# Space complexity: O(n*k)
# Stable
def counting_sort_for_radix(arr, k, get_digit):
    k += 1
    aux = [deque() for _ in range(k)]
    for i in arr:
        aux[get_digit(i)].append(i)
    i = 0
    for j in range(k):
        while len(aux[j]) > 0:
            arr[i] = aux[j].popleft()
            i += 1
