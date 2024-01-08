def extract(arr: list):
    ans = arr[0]
    arr[0] = arr[-1]
    arr.pop()
    sift_down(arr, 0)
    return ans


def sift_down(arr: list, pos):
    
    while 2 * pos + 2 < len(arr):
        if arr[2 * pos + 1] < arr[2 * pos + 2]:
            min_son_pos = 2 * pos + 1
        else:
            min_son_pos = 2 * pos + 2
        if arr[pos] > arr[min_son_pos]:
            arr[pos], arr[min_son_pos] =\
                arr[min_son_pos], arr[pos]
            pos = min_son_pos
        else:
            break
    if 2 * pos + 1 < len(arr) and arr[pos] > arr[2 * pos + 1]:
        arr[pos], arr[2 * pos + 1] =\
            arr[2 * pos + 1], arr[pos]
        
def heapify(arr: list):
    for i in range((len(arr) - 2) // 2, -1, -1):
        sift_down(arr, i)



n = int(input())
arr = list(map(int, input().split()))

heapify(arr)
for i in range(len(arr)):
    print(extract(arr), end=" ")

