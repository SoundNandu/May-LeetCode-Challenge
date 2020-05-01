You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

Example:

Given n = 5, and version = 4 is the first bad version.

call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true

Then 4 is the first bad version. 

Time:O(log n) Space:O(1)

#Here I have used Binary Search 

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low , high = 1,n
        while(low<=high):
        #calculate the mid value and the previous mid value contains in API 
            mid = (low+high)//2
            if isBadVersion(mid) and not isBadVersion(mid-1):
                return mid
        #mid is not equal to the version or greater move the low pointer
            elif not isBadVersion(mid):
                low = mid+1
         #Or move the high pointer
            else:
                high = mid-1
        return 1
            
