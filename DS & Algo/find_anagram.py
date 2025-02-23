#
# 438. Find All Anagrams in a String
# Given two strings s and p, return an array of all the start indices of p's anagrams
# in s. You may return the answer in any order.
#
#
'''
    Example 1:

    Input: s = "cbaebabacd", p = "abc"
    Output: [0,6]
    Explanation:
    The substring with start index = 0 is "cba", which is an anagram of "abc".
    The substring with start index = 6 is "bac", which is an anagram of "abc"
'''
from collections import Counter

def findAnagrams(self, s1: str, s2: str):
        s2_count = Counter(s2)
        window = Counter(s1[:len(s2)])
        result = [0] if window == s2_count else []

        for i in range(len(s2), len(s1)):
            window[s1[i]] += 1
            window[s1[i - len(s2)]] -= 1
            if window[s1[i - len(s2)]] == 0:
                del window[s1[i - len(s2)]]
            if window == s2_count:
                result.append(i - len(s2) + 1)

        return result


s = "cbaebabacd"
p = "abc"

def generate_test_cases():
    test_cases = [
        {"s": "cbaebabacd", "p": "abc", "expected_output": [0, 6]},
        {"s": "abab", "p": "ab", "expected_output": [0,1, 2]},
        {"s": "baa", "p": "aa", "expected_output": [1]},
        {"s": "hello", "p": "ll", "expected_output": [2]}
    ]

    return test_cases

test_cases = generate_test_cases()

for i, case in enumerate(test_cases):
    print(f"Test Case {i+1}:")
    print(f"s = {case['s']}")
    print(f"p = {case['p']}")
    expected_output = case["expected_output"]

    actual_output = findAnagrams(None, case["s"], case["p"])

    if actual_output == expected_output:
        print("Output matches the expected output.")
    else:
        print("Error: Output does not match the expected output.")

    print()
