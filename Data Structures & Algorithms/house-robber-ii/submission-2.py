class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # want to run a loop twice
        # 1: including first house and not last
        # 2: including last house and not first

        # maybe issue: if n == 3.....

        n = len(nums)

        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        firstHouse = [0] * (n - 1)
        lastHouse = [0] * (n - 1)

        firstHouse[0] = nums[0]
        firstHouse[1] = max(nums[0], nums[1])

        lastHouse[0] = nums[1]
        lastHouse[1] = max(nums[1], nums[2])

        def helper(house, offset):
            for i in range(2, len(house)):
                house[i] = max(house[i - 1], nums[i + offset] + house[i - 2])
            return house[-1]

        return max(helper(firstHouse, 0), helper(lastHouse, 1))

            

        


