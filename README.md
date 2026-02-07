<p align="center">
  <img src="https://github.com/anshkunj/hashmap-prefix-patterns/blob/0bbf91dbb47d55f1ca2af9b8fbf11698caae30f7/file_000000000e5c71fa9f1fbe9568a479f8.png" alt="Hashmap Prefix Patterns" width="1200">
</p>

<h1 align="center">Hashmap Prefix Patterns</h1>
<p align="center">Learn common prefix + hashmap patterns for efficient algorithm design 🚀</p>

# 🚀 HashMap & Prefix Sum Patterns

A curated collection of **HashMap and prefix sum algorithm problems** covering frequency counting, cumulative sums, and analytics challenges. Each solution is optimized, explained with examples, and mapped to real-world scenarios like log processing, data streams, and array manipulation.

---

## 🧠 Features
- Well-structured Python solutions  
- Optimized O(n) algorithms (no brute force  
- Clear explanation of hashmap & 
- ASCII diagrams showing algorithm flow  
- JSON-friendly examples where applicable  

---

## 📂 Repo Structure
```
hashmap-prefix-patterns/  
├── main.py          # FastAPI app & routes
├── logic.py         # Core algorithm implementations  
├── models.py        # Pydantic request models  
├── .gitignore  
├── requirements.txt  
├── render.yaml  
├── README.md       # Project Overview 
└── LICENSE        # Licence file (MIT)  
```
---

## 🏗️ How This Repo Works  
- logic.py contain logic of all problems  
- HashMap / prefix sum logic explained  
- Key patterns highlighted for **real-world applications**  
- Focus on cumulative sum, frequency counting, and O(n) optimizations  

---

## 📌 Problem Patterns Covered
- Subarray / substring sum equals K  
- Count pairs / triplets / quadruplets using HashMap  
- Duplicate detection & frequency counting  
- Prefix sum with constraints  
- Handling negative numbers and large inputs  

---

## ⚙️ Installation & Run

1) Clone the repository  
git clone https://github.com/anshkunj/hashmap-prefix-patterns.git  
cd hashmap-prefix-patterns  

2) Install dependencies  
pip install -r requirements.txt  

3) Run the server  
uvicorn main:app --reload  

---

## 🌐 API Documentation

Swagger UI: http://127.0.0.1:8000/docs  

ReDoc: http://127.0.0.1:8000/redoc  

---

## 🌐 Live API

Base URL: https://hashmap-prefix-patterns.onrender.com  
Docs: https://hashmap-prefix-patterns.onrender.com/docs

---

## 🔗 Endpoints – Prefix Sum & HashMap Patterns

This section documents conceptual API-style endpoints mapped directly to the functions in logic.py.
Each endpoint shows example input and expected output.

### 1️⃣ Two Sum
Endpoint: /hashmap/two-sum

Input:
nums = [2, 7, 11, 15]
target = 9

Output:
indices = [0, 1]

### 2️⃣ Happy Number
Endpoint: /hashmap/happy-number

Input:
n = 19

Output:
isHappy = true

### 3️⃣ Contains Duplicate II
Endpoint: /hashmap/contains-nearby-duplicate

Input:
nums = [1, 2, 3, 1]
k = 3

Output:
exists = true

### 4️⃣ Subarray Sum Equals K
Endpoint: /prefix/subarray-sum-k

Input:
nums = [1, 2, 3]
k = 3

Output:
count = 2

### 5️⃣ Group Anagrams
Endpoint: /hashmap/group-anagrams

Input:
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

Output:
groups = [["eat","tea","ate"],["tan","nat"],["bat"]]

### 6️⃣ Top K Frequent Elements
Endpoint: /hashmap/top-k-frequent

Input:
nums = [1,1,1,2,2,3]
k = 2

Output:
elements = [1, 2]

### 7️⃣ Contiguous Array
Endpoint: /prefix/contiguous-array

Input:
nums = [0, 1, 0, 1]

Output:
maxLength = 4

### 8️⃣ Subarray Sum Equals K (Alternative Implementation)
Endpoint: /prefix/subarray-sum-k-alt

Input:
nums = [1, 1, 1]
k = 2

Output:
count = 2

### 9️⃣ Binary Subarrays With Sum
Endpoint: /prefix/binary-subarrays-with-sum

Input:
nums = [1, 0, 1, 0, 1]
goal = 2

Output:
count = 4

### 1️⃣0️⃣ K-diff Pairs in Array
Endpoint: /hashmap/k-diff-pairs

Input:
nums = [3, 1, 4, 1, 5]
k = 2

Output:
pairs = 2

### 1️⃣1️⃣ Longest Subarray of 1s After Deleting One Element
Endpoint: /sliding-window/longest-subarray-after-delete-one

Input:
nums = [1, 1, 0, 1]

Output:
length = 3

### 1️⃣2️⃣ Subarrays With K Different Integers
Endpoint: /hashmap/subarrays-with-k-distinct

Input:
nums = [1, 2, 1, 2, 3]
k = 2

Output:
count = 7

---

## 🚧 Edge Cases Handled
- Empty arrays / strings  
- Large input sizes (up to 10^5)  
- Negative numbers  
- Exact / at most K constraints  

---

## 🛠️ Tech Stack
- Python 3.x  
- Standard libraries (`collections`, `itertools`)  
- Optional: Jupyter Notebook for visualization  

---

## 📄 Licence
MIT Licence  

---

## 🤝 Contributing
Contributors are welcome!  
• Add new ```hashmap-prefix``` problems  
• Improve explanations  
• Optimise exists code  

---

## 👤 Author
**anshkunj**  
GitHub: https://github.com/anshkunj  
Fiverr: https://www.fiverr.com/s/xX9mNXB  
LinkedIn: https://linkedin.com/in/anshkunj 

---

## ⭐ Support
If you find this repo helpful, give it a star ⭐  
It motivates me to create more real-world algorithm projects 🚀  

---

## 🔹 Note
This repo is regularly updated with new HashMap and prefix sum problems and explanations.
