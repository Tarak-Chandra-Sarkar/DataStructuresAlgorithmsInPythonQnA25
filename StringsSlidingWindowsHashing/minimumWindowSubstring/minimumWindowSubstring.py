from collections import Counter, defaultdict

def minimunWindowSubstring(s, t):
    if not s or not t:
        return ""

    # Step 1: Required character counts
    t_count = Counter(t)
    window = defaultdict(int)
    have = 0
    need = len(t_count)  # unique characters needed

    res_len = float('inf')
    res = [0, 0]
    left = 0

    for right in range(len(s)):
        char = s[right]
        window[char] += 1

        # If current char meets required count
        if char in t_count and window[char] == t_count[char]:
            have += 1

        # Step 2 and 3: Shrink window if all chars matched
        while have == need:
            # Update result if it's smaller
            if (right - left + 1) < res_len:
                res = [left, right + 1]
                res_len = right - left + 1

            # Pop from left to try and shrink
            window[s[left]] -= 1
            if s[left] in t_count and window[s[left]] < t_count[s[left]]:
                have -= 1
            left += 1

    l, r = res
    return s[l:r] if res_len != float('inf') else ""


# Example
s , t =  "ADOBECODEBANC", "ABC"
result = minimunWindowSubstring(s, t)
print(result)
