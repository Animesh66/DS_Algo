function_call_count = 0


def fibonacci_recursion(number: int) -> int:
    """
    This method is the solution of fibonacci series with recusion withing using 
    dynamic programming. This is not using memoization technique of dynamic programming.
    This will make too many recusive calls whihc is inefficient.
    Time complexity for this solution is O(2^n)
    """
    global function_call_count
    # This counter value will provide the number of times the recusive function
    function_call_count += 1
    # is called when the function is called recursively.
    if number == 0 or number == 1:
        return number
    return fibonacci_recursion(number - 1) + fibonacci_recursion(number - 2)


# Initialize a list of 100 elements with none value for memoization.
memoization = [None] * 100
# Initialize a counter to caculate the number of recursive call as we provide the number.
function_call_memoization = 0


def fibonacci_memoization(number: int) -> int:
    """
    This is the optimize solution for the fibonacci solution using memoization technique.
    This is used in dynamic programming.
    Time complexity of this method is O(n) preciously 2n - 1 number for functon calls will be made.
    """
    # Keep track of the number of recusive calls perfromed for a function call.
    global function_call_memoization
    function_call_memoization += 1
    # If the recusive call value is already stored on the memoization
    # list then just return the value
    if memoization[number] is not None:
        return memoization[number]
    #  This is the base condition for recursion
    if number == 0 or number == 1:
        return number
    # Store the value of the recustive call in the memoization list
    memoization[number] = fibonacci_memoization(
        number - 1) + fibonacci_memoization(number - 2)

    #  Return the value of the memorization from the function call.
    return memoization[number]


print(fibonacci_recursion(20))
print(function_call_count)
print(fibonacci_memoization(20))
print(function_call_memoization)
