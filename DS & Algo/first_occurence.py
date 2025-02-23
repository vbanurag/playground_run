'''
28. Find the Index of the First Occurrence in a String

Given two strings needle and haystack,
return the index of the first occurrence of needle in haystack,
or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

'''

def strStr(haystack, needle):
    n = len(needle)
    for i in range(len(haystack)):
        if haystack[i] == needle[0] and haystack[i: i+n] == needle:
            return i
    return -1


# Test case 1:
assert strStr("sadbutsad", "sad") == 0

# Test case 2:
assert strStr("sadbutsad", "s") == 0

# Test case 3:
assert strStr("sadbutsad", "d") == 2

# Test case 4:
assert strStr("sadbutsad", "t") == 5
