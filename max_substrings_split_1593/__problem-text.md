# 1593. Split a String Into the Max Number of Unique Substrings
## Medium

Given a string `s`, return the maximum number of unique substrings that the given string can be split into.

You can split string `s` into any list of non-empty substrings, where the concatenation of the substrings forms the original string. However, you must split the substrings such that all of them are unique.

A substring is a contiguous sequence of characters within a string.

Example 1:
```plaintext
Input: s = "ababccc"
Output: 5
Explanation: One way to split maximally is ['a', 'b', 'a', 'b', 'ccc']. Splitting like ['a', 'b', 'a', 'bc', 'cc'] is not valid as you have 'bc' and 'cc' that are the same.
```

Example 2:
```plaintext
Input: s = "aba"
Output: 2
Explanation: One way to split maximally is ['a', 'ba'].
```

Example 3:
```plaintext
Input: s = "aa"
Output: 1
Explanation: It is impossible to split the string any further.
```

Constraints:
- 1 <= s.length <= 16
- s contains only lower case English letters.

## Approach
We can solve this problem by using a recursive backtracking algorithm. We can start by iterating through the string and trying to split the string at each index. We can then check if the substring formed by splitting the string at the current index is unique. If it is unique, we can recursively call the function on the remaining part of the string and keep track of the maximum number of unique substrings we can form.

To check if a substring is unique, we can use a set to store all the substrings we have seen so far. If we encounter a substring that is already in the set, we can return 0, indicating that the current split is invalid.

We can keep track of the maximum number of unique substrings we can form by using a global variable. We can update this variable whenever we find a valid split that forms more unique substrings than the current maximum.

# Complexity Analysis
The time complexity for this approach is O(2^n), where n is the length of the input string s. This is because for each character in the string, we have two choices: either split the string at that index or not split the string at that index. This results in a total of 2^n possible splits.

The space complexity for this approach is O(n), where n is the length of the input string s. This is because we are using a set to store the substrings we have seen so far, and the maximum depth of the recursive call stack is equal to the length of the input string.

# Expected Implementation (Python)
We will implement the `maxUniqueSplit` function that takes a string `s` as input and returns the maximum number of unique substrings that the given string can be split into.

```python
def maxUniqueSplit(s):
    def backtrack(start, seen):
        nonlocal max_unique
        if start == len(s):
            max_unique = max(max_unique, len(seen))
            return
        for i in range(start, len(s)):
            sub = s[start:i + 1]
            if sub not in seen:
                seen.add(sub)
                backtrack(i + 1, seen)
                seen.remove(sub)

    max_unique = 0
    backtrack(0, set())
    return max_unique
```