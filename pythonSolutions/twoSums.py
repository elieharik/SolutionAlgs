class Solution(object):
    def twoSums(nums, target):
        """
        nums: List[int]
        target: int
        return type of twoSums: List[int]
        """
        for index1, element1 in enumerate(nums):
            # if element1 < target: ## Commented out - what if target is negative and element1 is positive
                for index2, element2 in enumerate(nums[index1+1:]):
                    if element1 + element2 == target:
                        # Adding offset (equal to index1 + 1) to index2; because enumerating starting at index1 + 1
                        return [index1, (index2+index1+1)]
        return [-1,-1]
        """
        O(n^2) Time | O(n) Space
        """

    def aBetterTwoSums(nums, target):
        # Use a dict., populate it with all the integers in the input list
        # When going through list, calculate complement and look for
        # complement in dict.
        indices = range(0, len(nums))
        complements = dict(zip(nums, indices))

        for index1, number in enumerate(nums):
            comp = target - number
            if (comp in complements) and (complements[comp] != index1):
                return [index1, complements[comp]]
        return[-1,-1]
        """
        O(n) | O(n) (dict space); runs in 42ms (67.7 percentile for python subs.)
        """

    ## Test twoSums function:
    # inputTwoSums = [3,2,4]
    # target = 6
    # result = aBetterTwoSums(inputTwoSums, target)
    # print(result)
