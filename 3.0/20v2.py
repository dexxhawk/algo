def extract(arr: list):
    ans = arr[0]
    arr[0] = arr[-1]
    arr.pop()
    sift_down(arr, 0)
    return ans


def sift_down(arr: list, pos):
    while 2 * pos + 1 < len(arr):
        #Choosing min son:
        min_son_idx = 2 * pos + 1
        if 2 * pos + 2 < len(arr) and arr[2 * pos + 2] < arr[min_son_idx]:
            min_son_idx = 2 * pos + 2

        if arr[pos] > arr[min_son_idx]:
            arr[pos], arr[min_son_idx] =\
                arr[min_son_idx], arr[pos]
            pos = min_son_idx
        else:
            break
        
def heapify(arr: list):
    for i in range((len(arr) - 2) // 2, -1, -1):
        sift_down(arr, i)


n = int(input())
arr = list(map(int, input().split()))

heapify(arr)
for i in range(len(arr)):
    print(extract(arr), end=" ")
