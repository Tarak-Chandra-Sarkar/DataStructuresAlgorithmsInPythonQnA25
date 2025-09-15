def longestSubstringWithoutRepeatingChars(s):
    charMap = {}           # Dictionary to store the last seen index of each character
    left = 0               # Left pointer of the current substring window
    maxLength = 0          # Stores the length of the longest valid substring found

    for right in range(len(s)):  # Iterate through each character in the string using right pointer
        # If current character is already seen and is inside the current window
        if s[right] in charMap and charMap[s[right]] >= left:
            left = charMap[s[right]] + 1  # Move left pointer to one position after last seen index

        charMap[s[right]] = right  # Update the last seen index of the current character

        # Calculate the length of the current window and update maxLength if it's larger
        maxLength = max(maxLength, right - left + 1)


    return maxLength  # Return the length of the longest substring without repeating characters



# Example Usage
s = "abcabcbb"
result = longestSubstringWithoutRepeatingChars(s)
print(result)