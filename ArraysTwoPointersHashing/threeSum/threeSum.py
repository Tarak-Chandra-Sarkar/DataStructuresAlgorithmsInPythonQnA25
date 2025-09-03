def threeSum(nums):
    # Step 1: Sort the array to use the two-pointer approach efficiently
    nums.sort()

    result = []  # This will store the unique triplets
    n = len(nums)

    # Step 2: Iterate through the array, fixing one element at a time
    for i in range(n):
        # Step 3: Skip duplicate elements to avoid repeating triplets
        if i > 0 and nums[i] == nums[i - 1]:
            continue  # Skip the same number we've already used as a starting point

        # Step 4: Set up two pointers
        left = i + 1         # Start just after the current index
        right = n - 1        # Start at the end of the array

        # Step 5: While left pointer is before the right
        while left < right:
            total = nums[i] + nums[left] + nums[right]  # Calculate the sum of the triplet

            if total < 0:
                # Step 6: If the sum is too small, move left pointer right to increase the sum
                left += 1
            elif total > 0:
                # Step 7: If the sum is too large, move right pointer left to decrease the sum
                right -= 1
            else:
                # Step 8: Found a valid triplet
                result.append([nums[i], nums[left], nums[right]])

                # Step 9: Skip duplicate values for left pointer
                while left < right and nums[left] == nums[left + 1]:
                    left += 1

                # Step 10: Skip duplicate values for right pointer
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                # Step 11: Move both pointers inward after finding a valid triplet
                left += 1
                right -= 1

    # Step 12: Return the list of unique triplets
    return result


# Example Usage
nums = [-1, 0, 1, 2, -1, -4]
result = threeSum(nums)
print(result)  
# Output: [[-1, -1, 2], [-1, 0, 1]]

# Reference Hints & Solutions 
# https://neetcode.io/solutions/3sum