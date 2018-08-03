from TDAs.heap import Heap


def heap_sort(arr):
    heap = Heap.heapify(arr, lambda x, y: x > y)
    for i in range(len(arr) - 1, 0, -1):
        heap.swap(0, i)
        heap.len -= 1
        heap.downheap(0)