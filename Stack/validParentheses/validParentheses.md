## Valid Parentheses

You are given a string <code>s</code> consisting of the following characters: <code>'(', ')', '{', '}', '[' and ']'</code>.

The input string <code>s</code> is valid if and only if:

- Every open bracket is closed by the same type of close bracket.
- Open brackets are closed in the correct order.
- Every close bracket has a corresponding open bracket of the same type.

Return <code>true</code> if s is a valid string, and <code>false</code> otherwise.<br>
 
### Example 1:
- Input: <code>s = "[]"</code>
- Output: <code>true</code>

### Example 2:
- Input: <code>s = "([{}])"</code>
- Output: <code>true</code>

### Example 3:
- Input: <code>s = "[(])"</code>
- Output: <code>false</code>
- Explanation: The brackets are not closed in the correct order. 

### Constraints:

<code>1 <= s.length <= 1000</code>

### [Leetcode Problem Link](https://leetcode.com/problems/valid-parentheses)

### [Solution in Python Link](validParentheses.py)
