
'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n))

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.


Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
'''

class Solution():
    def findMedianSortedArrays(self,nums1,nums2):
        m = len(nums1)
        n = len(nums2)

        sorteado = sorted(nums1 + nums2)

        if len(sorteado)%2 != 1:
            #print(len(sorteado)%2)

            #print('par')
            #print(f'primeiro {sorteado[int((m+n)/2)]}')
            #print(f'segundo {sorteado[int((m+n)/2 - 1)]}')

            a = float((sorteado[(m+n)//2 - 1] + sorteado[(m+n)//2]))/2
            #print(f'final {a}')

        else:
            #print('ímpar')
            a = sorteado[int((m+n)/2)]
            #print(f'final {a}')


        return a



a = [1,2]
b = [3,4]

solution = Solution()
result = solution.findMedianSortedArrays(a,b)
print(result)