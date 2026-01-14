"""
models.py
Contains Pydantic models for API requests
"""

from pydantic import BaseModel
from typing import List

# For array + k type problems
class ArrayKInput(BaseModel):
    nums: List[int]
    k: int

# For array + target problems
class ArrayTargetInput(BaseModel):
    nums: List[int]
    target: int

# For string + k problems
class StringKInput(BaseModel):
    s: str
    k: int

# For string list problems (like anagrams)
class StringListInput(BaseModel):
    strs: List[str]

# For binary array + goal
class BinaryGoalInput(BaseModel):
    nums: List[int]
    goal: int