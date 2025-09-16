## Minimum Window Substring

- Given two strings <code>s</code> and <code>t</code> of lengths m and n respectively, return the <b>minimum window substring</b> of s such that every character in t (<b>including duplicates</b>) is included in the window. <br>
If there is no such substring, return the empty string <code>""</code>.<br>

The testcases will be generated such that the answer is <b>unique</b>.

 

### Example 1:
- Input: <code>s = "ADOBECODEBANC"</code>, <code>t = "ABC"</code>
- Output: <code>"BANC"</code>
- Explanation: The minimum window substring "BANC" includes <code>'A', 'B', and 'C'</code> from string t.

### Example 2:
- Input: <code>s = "a", t = "a"</code>
- Output: <code>"a"</code>
- Explanation: The entire string <code>s</code> is the minimum window.

### Example 3:
- Input: <code>s = "a", t = "aa"</code>
- Output: <code>""</code>
- Explanation: Both <code>'a'</code>s from <code>t</code> must be included in the window.
Since the largest window of s only has one <code>'a'</code>, return empty string.
 

### Constraints:

<code>m == s.length</code>
<code>n == t.length</code>
<code>1 <= m, n <= 105</code>
<code>s</code> and <code>t</code> consist of uppercase and lowercase English letters.
 

Follow up: Could you find an algorithm that runs in <code>O(m + n)</code> time?

### [Leetcode Problem Link](https://leetcode.com/problems/minimum-window-substring)

### [Solution in Python Link](minimumWindowSubstring.py)
