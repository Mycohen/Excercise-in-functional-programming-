from functools import reduce


# Exercise 2 in Functional programming


# Question 1

# 1.1
def pentaNumRange(n1, n2):
    """Returns a list of pentagonal numbers within the range [n1, n2).

    Args:
    n1 (int): Lower bound of the range.
    n2 (int): Upper bound of the range.

    Returns:
    list: List of pentagonal numbers.
    """
    getPentaNum = lambda n: n * (3 * n - 1) // 2
    return list(map(getPentaNum, range(n1, n2)))


# 1.2
def nonFuncPenta():
    """Prints pentagonal numbers within a user-defined range using non-functional approach."""
    try:
        n1 = int(input("Enter n1: "))
        n2 = int(input("Enter n2: "))
        if n1 < 0 or n2 < 0:
            raise ValueError("n1 and n2 must be non-negative")
        elif n1 >= n2:
            raise ValueError("n1 must be less than n2")

        result = pentaNumRange(n1, n2)
        count = 0
        for i in result:
            print(i, end=", ")
            count += 1
            if count % 10 == 0:
                print()  # Print a newline after every 10 numbers

        print()  # Print a newline at the end
    except ValueError as e:
        print(f"Invalid input: {e}")


# 1.3
def checkNumbers(n1, n2):
    """Checks if n1 and n2 are positive integers and n2 > n1.

    Args:
    n1 (int): First number.
    n2 (int): Second number.

    Returns:
    bool: True if conditions are met, False otherwise.
    """
    return n2 >= 0 and n1 >= 0 and n2 > n1


def functionalPenta(n1, n2):
    """Returns a list of pentagonal numbers within the range [n1, n2) using a functional approach.

    Args:
    n1 (int): Lower bound of the range.
    n2 (int): Upper bound of the range.

    Returns:
    list: List of pentagonal numbers.
    """
    return list(map(lambda n: n * (3 * n - 1) // 2, range(n1, n2)))


def recursivePrint(myList):
    """Recursively prints elements of a list, 10 per line.

    Args:
    myList (list): List of elements to print.
    """
    if len(myList) <= 10:
        print(myList)
    else:
        print(myList[:10])
        recursivePrint(myList[10:])


def functionalPentaRange():
    """Prompts user for n1 and n2, checks validity, and prints pentagonal numbers within the range [n1, n2)."""
    try:
        n1 = int(input("Enter the value of n1: "))
        n2 = int(input("Enter the value of n2: "))
        if not checkNumbers(n1, n2):
            print("ERROR: the values must be positive integers and n2 > n1")
            return
        else:
            myList = functionalPenta(n1, n2)
            recursivePrint(myList)
    except ValueError:
        print("ERROR: Input is incorrect!")


# 2.1
def sumDigits(n: int):
    """Calculates the sum of digits of an integer.

    Args:
    n (int): Input integer.

    Returns:
    int: Sum of digits.
    """
    return sum(splitDigits(n))


def splitDigits(n: int):
    """Splits an integer into its constituent digits.

    Args:
    n (int): Input integer.

    Returns:
    list: List of digits.
    """
    return list(map(int, str(abs(n))))


# 2.2
def applySum():
    """Prompts user for an integer, calculates and prints the sum of its digits."""
    try:
        n = int(input("Enter an integer number n (positive or negative): "))
        print(sumDigits(n))
    except ValueError:
        print("ERROR: Input is incorrect!")


# 2.3
def reverseNumber(n: int):
    """Reverses the digits of an integer.

    Args:
    n (int): Input integer.

    Returns:
    str: Reversed digits as a string.
    """
    return str(abs(n))[::-1]


# 3.1
def isPalindrome(n: int):
    """Checks if an integer is a palindrome.

    Args:
    n (int): Input integer.

    Returns:
    bool: True if the integer is a palindrome, False otherwise.
    """
    return reverseNumber(n) == str(abs(n))


# 3.2
def checkPalindrome():
    """Prompts user for an integer, checks and prints if it is a palindrome."""
    try:
        n = int(input("Enter an integer number n (positive or negative): "))
        if isPalindrome(n):
            print("It is a palindrome")
        else:
            print("It is not a palindrome")
    except ValueError:
        print("ERROR: Input is incorrect!")


# 4.1
def m(i):
    """Defines a function m(i) as per Exercise 4.1."""
    if i == 1:
        return -0.5
    return i / (i + 1)


def my(n):
    """Defines a function my(n) as per Exercise 4.1."""
    return list(map(lambda x: m(x) + 1, range(1, n + 1)))


def anotherRecursivePrint(param, n=1):
    """Recursive print function for Exercise 4.2."""
    if len(param) == 1:
        print(f"{n} {param[0]}")
    else:
        print(f"{n} {param[0]}")
        anotherRecursivePrint(param[1:], n + 1)


def process_number():
    """Prompts user for a natural number n, calculates and recursively prints results of my(n)."""
    try:
        n = int(input("Enter a natural number: "))
        if n <= 0:
            raise ValueError()
        anotherRecursivePrint(my(n))
    except ValueError:
        print("ERROR: Input is incorrect!")


# 5.1
def add3dicts(d1, d2, d3):
    """Merges three dictionaries and combines values for common keys into a tuple.

    Args:
    d1 (dict): First dictionary.
    d2 (dict): Second dictionary.
    d3 (dict): Third dictionary.

    Returns:
    dict: Merged dictionary.
    """
    d4 = set(d1.keys()).union(set(d2.keys())).union(set(d3.keys()))
    return {k: tuple({d.get(k, None) for d in (d1, d2, d3)}) for k in d4}


def test_add3dicts():
    """Tests the add3dicts function by taking input for three dictionaries and printing the merged result."""
    try:
        d1 = eval(input("Enter dictionary 1 (as Python dictionary literal): "))
        d2 = eval(input("Enter dictionary 2 (as Python dictionary literal): "))
        d3 = eval(input("Enter dictionary 3 (as Python dictionary literal): "))
        if not (isinstance(d1, dict) and isinstance(d2, dict) and isinstance(d3, dict)):
            raise ValueError("Input must be dictionaries.")

        merged_dict = add3dicts(d1, d2, d3)
        print("Merged Dictionary:", merged_dict)
    except (ValueError, SyntaxError) as e:
        print(f"ERROR: {e}")


def main():
    """Main function that implements a menu-driven interface for all exercises."""
    while True:
        print("\n=== Menu ===")
        print("1. Exercise 1 - Non-functional Penta Numbers")
        print("2. Exercise 2 - Functional Penta Numbers")
        print("3. Exercise 3 - Sum of Digits")
        print("4. Exercise 4 - Palindrome Check")
        print("5. Exercise 5 - Recursive Print of Function Results")
        print("6. Exercise 6 - Merge Three Dictionaries")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            nonFuncPenta()
        elif choice == '2':
            functionalPentaRange()
        elif choice == '3':
            applySum()
        elif choice == '4':
            checkPalindrome()
        elif choice == '5':
            process_number()
        elif choice == '6':
            test_add3dicts()
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number from the menu.")


if __name__ == "__main__":
    main()
