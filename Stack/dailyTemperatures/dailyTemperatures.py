def dailyTemperatures(temperatures):
    n = len(temperatures)          # Total number of days
    result = [0] * n               # Result array, default 0 for each day
    stack = []                     # Stack to store indices of days

    # Loop through each day
    for i in range(n):

        # While there are days in the stack AND
        # today's temperature is warmer than the temperature
        # of the day at the top of the stack
        while stack and temperatures[i] > temperatures[stack[-1]]:
            
            prev_day = stack.pop()     # Get the previous colder day index
            result[prev_day] = i - prev_day  # Number of days waited = current day - previous day

        # Push current day index onto the stack
        stack.append(i)

    # Days left in the stack have no warmer future day → remain 0
    return result



# Example
temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
result = dailyTemperatures(temperatures)
print(result)
