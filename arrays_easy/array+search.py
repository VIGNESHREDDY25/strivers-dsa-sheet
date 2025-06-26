'''Given an array, arr[] sorted in ascending order and an integer k. Return true if k is present in the array, otherwise, false.

Examples:

Input: arr[] = [1, 2, 3, 4, 6], k = 6
Output: true
Exlpanation: Since, 6 is present in the array at index 4 (0-based indexing), output is true.
Input: arr[] = [1, 2, 4, 5, 6], k = 3
Output: false
Exlpanation: Since, 3 is not present in the array, output is false.
Input: arr[] = [2, 3, 5, 6], k = 1
Output: false
Constraints:
1 <= arr.size() <= 106
1 <= k <= 106
1 <= arr[i] <= 106'''

#User function Template for python3
class Solution:
    ##Complete this function
    def searchInSorted(self,arr, k):
        #Your code here
        if len(arr)==0:
            return False
        if arr[len(arr)//2]>=k:
            for i in range(0,len(arr)//2+1):
                if k==arr[i]:
                    return True
                    break
        elif arr[len(arr)//2]<=k:
            for i in range(len(arr)//2,len(arr)):
                if k==arr[i]:
                    return True 
                    break
        else :
            return False