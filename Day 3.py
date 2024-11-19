class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        max_sum = 0
        current_sum = 0
        window_start = 0
        freq_map = {}

        for window_end in range(len(nums)):
            current_num = nums[window_end]
            current_sum += current_num
            freq_map[current_num] = freq_map.get(current_num, 0) + 1

            while freq_map[current_num] > 1:
                left_num = nums[window_start]
                current_sum -= left_num
                freq_map[left_num] -= 1
                if freq_map[left_num] == 0:
                    del freq_map[left_num]
                window_start += 1

            if window_end - window_start + 1 == k:
                max_sum = max(max_sum, current_sum)
                left_num = nums[window_start]
                current_sum -= left_num
                freq_map[left_num] -= 1
                if freq_map[left_num] == 0:
                    del freq_map[left_num]
                window_start += 1

        return max_sum


nums = [9, 9, 9, 1, 2, 3]
k = 3
solution = Solution()
print(solution.maximumSubarraySum(nums, k))  # Output: 12

