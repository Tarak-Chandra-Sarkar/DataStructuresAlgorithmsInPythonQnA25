def isValidParentheses(s: str) -> bool:
    stack = []  # Stack to keep track of opening brackets

    # Mapping of closing brackets to their matching opening brackets
    closetoOpenMapping = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    # Iterate through each character in the string
    for char in s:
        # If the character is a closing bracket
        if char in closetoOpenMapping:
            # Pop the top element from stack if not empty, else use a dummy value
            top = stack.pop() if stack else '#'

            # If the popped opening bracket does not match
            if closetoOpenMapping[char] != top:
                return False  # Invalid parentheses
        else:
            # If it's an opening bracket, push it onto the stack
            stack.append(char)

    # If stack is empty, all brackets were matched correctly
    return not stack


# Example
s = "[()}]"
result = isValidParentheses(s)
print(result)
