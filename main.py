"""
main.py
FastAPI app for HashMap & Prefix Sum Patterns Repo
All 12 problems exposed as API endpoints
"""

from fastapi import FastAPI
from logic import *
from models import *

app = FastAPI(title="HashMap & Prefix Sum Patterns API")

@app.get("/")
def root():
    return {"message": "Welcome to HashMap & Prefix Sum Patterns API!"}


# 1️⃣ Two Sum
@app.post("/two_sum")
def api_two_sum_post(input: ArrayTargetInput):
    return {"result": two_sum(input.nums, input.target)}

@app.get("/two_sum")
def api_two_sum_get(nums: str, target: int):
    nums_list = [int(x) for x in nums.split(",")]
    return {"result": two_sum(nums_list, target)}


# 2️⃣ Happy Number
@app.post("/happy_number")
def api_happy_number_post(input: ArrayTargetInput):
    # input.target used as the number n
    return {"result": is_happy(input.target)}

@app.get("/happy_number")
def api_happy_number_get(n: int):
    return {"result": is_happy(n)}


# 3️⃣ Contains Duplicate II
@app.post("/contains_duplicate_ii")
def api_contains_duplicate_post(input: ArrayKInput):
    return {"result": contains_nearby_duplicate(input.nums, input.k)}

@app.get("/contains_duplicate_ii")
def api_contains_duplicate_get(nums: str, k: int):
    nums_list = [int(x) for x in nums.split(",")]
    return {"result": contains_nearby_duplicate(nums_list, k)}


# 4️⃣ Subarray Sum Equals K
@app.post("/subarray_sum_equals_k")
def api_subarray_sum_post(input: ArrayTargetInput):
    return {"result": subarray_sum(input.nums, input.target)}

@app.get("/subarray_sum_equals_k")
def api_subarray_sum_get(nums: str, target: int):
    nums_list = [int(x) for x in nums.split(",")]
    return {"result": subarray_sum(nums_list, target)}


# 5️⃣ Group Anagrams
@app.post("/group_anagrams")
def api_group_anagrams_post(input: StringListInput):
    return {"result": group_anagrams(input.strs)}

@app.get("/group_anagrams")
def api_group_anagrams_get(strs: str):
    strs_list = strs.split(",")
    return {"result": group_anagrams(strs_list)}


# 6️⃣ Top K Frequent Elements
@app.post("/top_k_frequent")
def api_top_k_post(input: ArrayKInput):
    return {"result": top_k_frequent(input.nums, input.k)}

@app.get("/top_k_frequent")
def api_top_k_get(nums: str, k: int):
    nums_list = [int(x) for x in nums.split(",")]
    return {"result": top_k_frequent(nums_list, k)}


# 7️⃣ Contiguous Array
@app.post("/contiguous_array")
def api_contiguous_array_post(input: ArrayKInput):
    return {"result": find_max_length(input.nums)}

@app.get("/contiguous_array")
def api_contiguous_array_get(nums: str):
    nums_list = [int(x) for x in nums.split(",")]
    return {"result": find_max_length(nums_list)}


# 8️⃣ Subarray Sum Equals K (duplicate function)
@app.post("/subarray_sum_equals_k_duplicate")
def api_subarray_sum_dup_post(input: ArrayTargetInput):
    return {"result": subarray_sum_equals_k(input.nums, input.target)}

@app.get("/subarray_sum_equals_k_duplicate")
def api_subarray_sum_dup_get(nums: str, target: int):
    nums_list = [int(x) for x in nums.split(",")]
    return {"result": subarray_sum_equals_k(nums_list, target)}


# 9️⃣ Binary Subarrays With Sum
@app.post("/binary_subarrays_with_sum")
def api_binary_subarrays_post(input: BinaryGoalInput):
    return {"result": num_subarrays_with_sum(input.nums, input.goal)}

@app.get("/binary_subarrays_with_sum")
def api_binary_subarrays_get(nums: str, goal: int):
    nums_list = [int(x) for x in nums.split(",")]
    return {"result": num_subarrays_with_sum(nums_list, goal)}


# 1️⃣0️⃣ K-diff Pairs in Array
@app.post("/k_diff_pairs")
def api_k_diff_pairs_post(input: ArrayKInput):
    return {"result": find_pairs(input.nums, input.k)}

@app.get("/k_diff_pairs")
def api_k_diff_pairs_get(nums: str, k: int):
    nums_list = [int(x) for x in nums.split(",")]
    return {"result": find_pairs(nums_list, k)}


# 1️⃣1️⃣ Longest Subarray of 1’s After Deleting One Element
@app.post("/longest_subarray_after_delete")
def api_longest_subarray_post(input: ArrayKInput):
    return {"result": longest_subarray_after_delete_one(input.nums)}

@app.get("/longest_subarray_after_delete")
def api_longest_subarray_get(nums: str):
    nums_list = [int(x) for x in nums.split(",")]
    return {"result": longest_subarray_after_delete_one(nums_list)}


# 1️⃣2️⃣ Subarrays With K Different Integers
@app.post("/subarrays_with_k_distinct")
def api_subarrays_k_post(input: ArrayKInput):
    return {"result": subarrays_with_k_distinct(input.nums, input.k)}

@app.get("/subarrays_with_k_distinct")
def api_subarrays_k_get(nums: str, k: int):
    nums_list = [int(x) for x in nums.split(",")]
    return {"result": subarrays_with_k_distinct(nums_list, k)}