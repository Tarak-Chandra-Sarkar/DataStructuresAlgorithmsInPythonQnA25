## 3Sum

Given an integer array nums, return all the triplets <code>[nums[i], nums[j], nums[k]]</code> such that <br> <code>i != j</code>, <code>i != k</code>, and <code>j != k</code>, and <code>nums[i] + nums[j] + nums[k] == 0</code>.

Notice that <i>the solution set must not contain duplicate triplets.</i>
 

### Example 1:
- Input: <code>nums = [-1,0,1,2,-1,-4]</code>
- Output: <code>[[-1,-1,2],[-1,0,1]]</code>
- Explanation: <br>
<code>nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0. <br>
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0. <br>
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0. <br></code>
The distinct triplets are <code>[-1,0,1] and [-1,-1,2].</code> <br>
Notice that the order of the output and the order of the triplets does not matter.

### Example 2:
- Input: <code>nums = [0,1,1]</code>
- Output: <code>[]</code>
- Explanation: The only possible triplet does not sum up to <code>0</code>.

### Example 3:
- Input: <code>nums = [0,0,0]</code>
- Output: <code>[[0,0,0]]</code>
- Explanation: The only possible triplet sums up to <code>0</code>.
 

### Constraints:

- <code>3 <= nums.length <= 3000</code>
- <code>-105 <= nums[i] <= 105</code>

### [Leetcode Problem Link](https://leetcode.com/problems/3sum)

### [Solution in Python Link](threeSum.py)