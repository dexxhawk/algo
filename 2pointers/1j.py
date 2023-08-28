# def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
#     c = [0] * (m + n)
#     i = 0
#     j = 0
#     k = 0

#     while i < m or j < n:
#         if i >= m:
#             c[k] = nums2[j]
#             j += 1
#             k += 1
#         elif j >= n:
#             c[k] = nums1[i]
#             i += 1
#             k += 1
#         else:
#             if nums1[i] >= nums2[j]:
#                 c[k] = nums2[j]
#                 j += 1
#                 k += 1
#             else:
#                 c[k] = nums1[i]
#                 i += 1
#                 k += 1
#     print(*c, end=' ')

def merge(a: list[int], n: int, b: list[int], m: int) -> None:
    c = [0] * (m + n)
    i = 0
    j = 0

    while i < n or j < m:
        if j == m or i < n and a[i] < b[j]:
            c[i + j] = a[i]
            i += 1
        else:
            c[i + j] = b[j]
            j += 1
    print(*c, end=' ')

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
merge(a, n, b, m)
