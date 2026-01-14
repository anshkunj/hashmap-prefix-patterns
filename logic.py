"""
logic.py
Contains all HashMap & Prefix Sum problem solutions.
Each function is standalone and can be imported in main.py
"""

from collections import defaultdict
from typing import List

# 1️⃣ Two Sum
def two_sum(nums: List[int], target: int) -> List[int]:
    hashmap = {}
    for i, num in enumerate(nums):
        if target - num in hashmap:
            return [hashmap[target - num], i]
        hashmap[num] = i
    return []

# 2️⃣ Happy Number
def is_happy(n: int) -> bool:
    def sum_sq(x):
        return sum(int(d)**2 for d in str(x))
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum_sq(n)
    return n == 1

# 3️⃣ Contains Duplicate II
def contains_nearby_duplicate(nums: List[int], k: int) -> bool:
    hashmap = {}
    for i, num in enumerate(nums):
        if num in hashmap and i - hashmap[num] <= k:
            return True
        hashmap[num] = i
    return False

# 4️⃣ Subarray Sum Equals K
def subarray_sum(nums: List[int], k: int) -> int:
    count = 0
    prefix = {0:1}
    total = 0
    for num in nums:
        total += num
        count += prefix.get(total - k, 0)
        prefix[total] = prefix.get(total, 0) + 1
    return count

# 5️⃣ Group Anagrams
def group_anagrams(strs: List[str]) -> List[List[str]]:
    hashmap = defaultdict(list)
    for s in strs:
        key = tuple(sorted(s))
        hashmap[key].append(s)
    return list(hashmap.values())

# 6️⃣ Top K Frequent Elements
def top_k_frequent(nums: List[int], k: int) -> List[int]:
    freq = defaultdict(int)
    for num in nums:
        freq[num] += 1
    freq_sorted = sorted(freq.items(), key=lambda x: -x[1])
    return [num for num, _ in freq_sorted[:k]]

# 7️⃣ Contiguous Array
def find_max_length(nums: List[int]) -> int:
    prefix_map = {0: -1}
    max_len = 0
    count = 0
    for i, num in enumerate(nums):
        count += 1 if num == 1 else -1
        if count in prefix_map:
            max_len = max(max_len, i - prefix_map[count])
        else:
            prefix_map[count] = i
    return max_len

# 8️⃣ Subarray Sum Equals K (duplicate, same as 4)
def subarray_sum_equals_k(nums: List[int], k: int) -> int:
    return subarray_sum(nums, k)

# 9️⃣ Binary Subarrays With Sum
def num_subarrays_with_sum(nums: List[int], goal: int) -> int:
    prefix = {0:1}
    total = 0
    count = 0
    for num in nums:
        total += num
        count += prefix.get(total - goal, 0)
        prefix[total] = prefix.get(total, 0) + 1
    return count

# 1️⃣0️⃣ K-diff Pairs in Array
def find_pairs(nums: List[int], k: int) -> int:
    hashmap = defaultdict(int)
    count = 0
    for num in nums:
        hashmap[num] += 1
    for num in hashmap:
        if k > 0 and num + k in hashmap:
            count += 1
        elif k == 0 and hashmap[num] > 1:
            count += 1
    return count

# 1️⃣1️⃣ Longest Subarray of 1’s After Deleting One Element
def longest_subarray_after_delete_one(nums: List[int]) -> int:
    l = 0
    zero_count = 0
    max_len = 0
    for r in range(len(nums)):
        if nums[r] == 0:
            zero_count += 1
        while zero_count > 1:
            if nums[l] == 0:
                zero_count -= 1
            l += 1
        max_len = max(max_len, r - l)
    return max_len

# 1️⃣2️⃣ Subarrays with K Different Integers
def subarrays_with_k_distinct(nums: List[int], k: int) -> int:
    def at_most(k):
        freq = defaultdict(int)
        l = 0
        res = 0
        for r in range(len(nums)):
            if freq[nums[r]] == 0:
                k -= 1
            freq[nums[r]] += 1
            while k < 0:
                freq[nums[l]] -= 1
                if freq[nums[l]] == 0:
                    k += 1
                l += 1
            res += r - l + 1
        return res
    return at_most(k) - at_most(k-1)