def insert(k: int):
    heap.append(k)
    pos = len(heap) - 1

    while pos > 0 and heap[pos] < heap[(pos - 1) // 2]:
        heap[pos], heap[(pos - 1) // 2] =\
            heap[(pos - 1) // 2], heap[pos]
        pos = (pos - 1) // 2

def extract():
    ans = heap[0]
    heap[0] = heap[-1]
    heap.pop()

    #Siftdown:
    pos = 0
    while 2 * pos + 1 < len(heap):
        #Choosing min son:
        min_son_idx = 2 * pos + 1
        if 2 * pos + 2 < len(heap) and heap[2 * pos + 2] < heap[min_son_idx]:
            min_son_idx = 2 * pos + 2

        if heap[pos] > heap[min_son_idx]:
            heap[pos], heap[min_son_idx] =\
                heap[min_son_idx], heap[pos]
            pos = min_son_idx
        else:
            break
    return ans
# Можно сразу pop-нуть последний элемент, тогда если он останется, то возможны случаи:
# 1) в самом низу будет либо 2 листа, с собой мы элемент не поменяем => после while ничего не требуется
# 2) в самом низу будет только наш сам неудаленный элемент, мы с ним не поменяемся и потом удалим его.


heap = []

n = int(input())
arr = list(map(int, input().split()))

for i in range(n):
    insert(arr[i])
for i in range(n):
    print(extract(), end = " ")
