## Container With Most Water

- You are given an integer array <code>height</code> of length <code>n</code>. There are <code>n</code> vertical lines drawn such that the two endpoints of the <code>i<sup>th</sup></code> line are <code>(i, 0)</code> and <code>(i, height[i])</code>.

- Find two lines that together with the x-axis form a container, such that the container contains the most water.

- Return <i>the maximum amount of water a container can store</i>.

- Notice that you may not slant the container. 

### Example 1:
![alt text](maxWaterContainer.png)

- Input: <code>height = [1,8,6,2,5,4,8,3,7]</code>
- Output: <code>49</code>
- Explanation: <code>The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. <br>
  In this case, the max area of water (blue section) the container can contain is 49</code>.

### Example 2:

- Input: <code>height = [1,1]</code>
- Output: <code>1</code>
 

#### Constraints:

- <code>n == height.length</code>
- <code>2 <= n <= 105</code>
- <code>0 <= height[i] <= 104</code>

### [Leetcode Problem Link](https://leetcode.com/problems/container-with-most-water)

### [Solution in Python Link](maxWaterContainer.py)