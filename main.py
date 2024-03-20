from typing import List


#
#
# def findPeaks(mountain: List[int]) -> List[int]:
#     res = []
#     for i in range(1, len(mountain) - 1):
#         if mountain[i] > mountain[i - 1] and mountain[i] > mountain[i + 1]:
#             res.append(i)
#     return res
#
#
# print(findPeaks([1, 4, 3, 8, 5]))


# def minimumAddedCoins(coins: List[int], target: int) -> int:
#     coins.sort()
#     total = 0
#
#     coin = summ = 0
#     for x in range(1, target + 1):
#         if coin < len(coins) and coins[coin] <= x:
#             summ += coins[coin]
#             coin += 1
#         elif summ < x:
#             summ += x
#             total += 1
#     return total
#
#
# print(minimumAddedCoins([1, 4, 10], 19))


def findIntersectionValues(nums1: List[int], nums2: List[int]) -> List[int]:
    count = 0
    out = []
    for i in nums1:
        if i in nums2:
            count += 1
    out.append(count)
    count1 = 0
    for i in nums2:
        if i in nums1:
            count1 += 1
    out.append(count1)
    return out


print(findIntersectionValues([4, 3, 2, 3, 1], [2, 2, 5, 2, 3, 6]))
