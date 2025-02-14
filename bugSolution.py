def function_with_uncommon_error_solution(x, y):
    if x == 0:
        return float('inf') # Or handle the error with a different approach like returning a specific value, or raising a custom exception
    else:
        return x / y