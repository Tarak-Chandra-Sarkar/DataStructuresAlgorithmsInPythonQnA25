## Longest Consecutive Sequence

- Given an unsorted array of integers <code>nums</code>, return the length of the longest consecutive elements sequence.

- You must write an algorithm that runs in <code>O(n)</code> time.

 

### Example 1:

- Input: <code>nums = [100,4,200,1,3,2]</code>
- Output: <code>4</code>
- Explanation: The longest consecutive elements sequence is <code>[1, 2, 3, 4]. Therefore its length is 4.</code>

### Example 2:
- Input: <code>nums = [0,3,7,2,5,8,4,6,0,1]</code>
- Output: <code>9</code>

### Example 3:
- Input: <code>nums = [1,0,1,2]</code>
- Output: <code>3</code>
 

### Constraints:

- <code>0 <= nums.length <= 105</code>
- <code>-109 <= nums[i] <= 109</code>

```python
def longestConsecutiveSequence(nums: list[int]) -> int:
        # Step 1: Use a set for O(1) lookups
        numSet = set(nums)

        # Step 2: Initialize variable to track the longest sequence
        longest = 0

        # Step 3: Iterate over each number
        for num in numSet:
            # Only try to build sequence from numbers that are the start of a sequence
            if (num - 1) not in numSet:
                # This means 'num' is the start of a new sequence
                length = 1

                # Step 4: Expand the sequence
                while (num + length) in numSet:
                    length += 1
                
                # Step 5: Update the result if we found a longer streak
                longest = max(length, longest)

        # Step 6: Return the longest sequence length found
        return longest


# Examples & test
print("Example")
nums = [2,20,4,10,3,4,5]
result = longestConsecutiveSequence(nums)
print(result)

```