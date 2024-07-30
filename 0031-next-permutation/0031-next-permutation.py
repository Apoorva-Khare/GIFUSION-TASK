class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # finding the decreasing element from the end
        i = len(nums) - 2

        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        if i >= 0:      #if the entire array is not in descending order
            # find the element just larger than nums[i]
            j = len(nums) - 1

            while nums[j] <= nums[i]:
                j -= 1
            #swap elements at i and j
            nums[i], nums[j] = nums[j], nums[i]

        #reverse the sequence after ith index
        nums[i +1:] = reversed(nums[i + 1:])
               