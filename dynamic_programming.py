function_call_count = 0


def fibonacci_recursion(number: int) -> int:
    """
    This method is the solution of fibonacci series with recusion withing using 
    dynamic programming. This is not using memoization technique of dynamic programming.
    This will make too many recusive calls whihc is inefficient.
    """
    global function_call_count
    # This counter value will provide the number of times the recusive function
    function_call_count += 1
    # is called when the function is called recursively.
    if number == 0 or number == 1:
        return number
    return fibonacci_recursion(number - 1) + fibonacci_recursion(number - 2)


print(fibonacci_recursion(20))
print(function_call_count)
