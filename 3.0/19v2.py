def insert(k: int):
    heap.append(k)
    pos = len(heap) - 1

    while pos > 0 and heap[pos] > heap[(pos - 1) // 2]:
        heap[pos], heap[(pos - 1) // 2] =\
            heap[(pos - 1) // 2], heap[pos]
        pos = (pos - 1) // 2

def extract():
    ans = heap[0]
    heap[0] = heap[-1]
    heap.pop()

    pos = 0
    while 2 * pos + 2 < len(heap):
        if heap[2 * pos + 1] > heap[2 * pos + 2]:
            max_son_idx = 2 * pos + 1
        else:
            max_son_idx = 2 * pos + 2
        if heap[pos] < heap[max_son_idx]:
            heap[pos], heap[max_son_idx] =\
                heap[max_son_idx], heap[pos]
            pos = max_son_idx
        else:
            break
    if 2 * pos + 1 < len(heap) and heap[pos] < heap[2 * pos + 1]:
        heap[pos], heap[2 * pos + 1] = heap[2 * pos + 1], heap[pos]
    return ans
# Можно сразу pop-нуть последний элемент, тогда если он останется, то возможны случаи:
# 1) в самом низу будет либо 2 листа, с собой мы элемент не поменяем => после while ничего не требуется
# 2) в самом низу будет только наш сам неудаленный элемент, мы с ним не поменяемся и потом удалим его.


heap = []

n = int(input())
for i in range(n):
    cmd = input().split()
    
    if cmd[0] == "0":
        insert(int(cmd[1]))
    else:
        print(extract())

