from statistics import median
from typing import List


class MedianOfTwoSortedArrays:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        joinedlist = sorted(nums1 + nums2)
        if len(joinedlist) == 1:
            return joinedlist[0]
        if len(joinedlist) % 2 == 0:
            return (joinedlist[len(joinedlist)//2] + joinedlist[(len(joinedlist)//2 - 1)]) / 2
        else:
            return joinedlist[len(joinedlist)//2]

    def findMedianSortedArraysWithLibrairies(self, nums1: List[int], nums2: List[int]) -> float:
        return median(sorted(nums1 + nums2))



def test_solution():
    m = MedianOfTwoSortedArrays()
    print(m.findMedianSortedArraysWithLibrairies(list([1, 2]), list([3, 4])))


test_solution()
