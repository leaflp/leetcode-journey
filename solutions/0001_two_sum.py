# 题号：0001  难度：Easy
# 题目：两数之和
# 日期：2026-04-01
# 理解：用字典记录每个数的位置，遇到目标差值就返回

class Solution:
    def twoSum(self, nums, target):
        seen = {}
        for i, n in enumerate(nums):
            if target - n in seen:
                return [seen[target - n], i]
            seen[n] = i
# 本地测试
s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))   # 期望输出 [0, 1]
print(s.twoSum([3, 2, 4], 6))         # 期望输出 [1, 2]