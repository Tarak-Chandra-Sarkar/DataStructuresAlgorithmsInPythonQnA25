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

