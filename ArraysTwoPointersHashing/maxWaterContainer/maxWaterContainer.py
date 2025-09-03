def maxWaterContainer(height):
    # Initialize two pointers at the beginning and end of the array
    left, right = 0, len(height) - 1
    
    # Variable to keep track of the maximum area found so far
    max_area = 0

    # Loop until the two pointers meet
    while left < right:
        # Height of the container is the shorter of the two lines
        h = min(height[left], height[right])

        # Width of the container is the distance between the two pointers
        w = right - left

        # Calculate the current area and update max_area if it's larger
        max_area = max(max_area, h * w)

        # Move the pointer pointing to the shorter line inward,
        # since moving the taller one can't increase the area
        if height[left] < height[right]:
            left += 1  # Move left pointer to the right
        else:
            right -= 1  # Move right pointer to the left

    # Return the maximum area found
    return max_area



#Example Usage:
heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
result = maxWaterContainer(heights)
print(result)  # Output: 49


# Reference Hints & Solutions
# https://neetcode.io/solutions/container-with-most-water