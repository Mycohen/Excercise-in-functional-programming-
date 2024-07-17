# File: functional_programming_exercises.py
# Author: Moshe Yaakov Cohen


from functools import reduce


# Exercise 1: Calculate factorial using recursion
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)


# Exercise 2: Calculate factorial using reduce and lambda
factorial_reduce = lambda n: reduce(lambda x, y: x * y, range(1, n + 1), 1)


# Exercise 3: Generate Fibonacci sequence using recursion
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# Exercise 4: Generate Fibonacci sequence using functional approach
def fibonacci_list(n):
    fib = lambda n: n if n <= 1 else fib(n - 1) + fib(n - 2)
    return [fib(i) for i in range(n)]


# Exercise 5: Check if a number is prime using functional approach
def is_prime(n):
    if n <= 1:
        return False
    return all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))


# Exercise 6: Filter prime numbers from a list
def filter_primes(numbers):
    return list(filter(is_prime, numbers))


# Exercise 7: Calculate sum of squares using map and lambda
def sum_of_squares(numbers):
    return sum(map(lambda x: x ** 2, numbers))


# Exercise 8: Reverse a string using recursion
def reverse_string(s):
    return s[::-1]


# Exercise 9: Reverse words in a string using functional approach
def reverse_words(s):
    return ' '.join(s.split()[::-1])


# Exercise 10: Count words in a string using reduce
def count_words(s):
    return len(s.split())


# Exercise 11: Calculate power of a number using recursion
def power(x, n):
    return 1 if n == 0 else x * power(x, n - 1)


# Exercise 12: Calculate power of a number using reduce and lambda
power_reduce = lambda x, n: reduce(lambda a, _: a * x, range(n), 1)


# Menu-driven interface to test exercises
def main():
    while True:
        print("\n=== Functional Programming Exercises ===")
        print("1. Factorial (recursive)")
        print("2. Factorial (using reduce and lambda)")
        print("3. Fibonacci Sequence (recursive)")
        print("4. Fibonacci Sequence (functional approach)")
        print("5. Check Prime Number")
        print("6. Filter Prime Numbers from List")
        print("7. Sum of Squares")
        print("8. Reverse String (recursive)")
        print("9. Reverse Words in String")
        print("10. Count Words in String")
        print("11. Power of Number (recursive)")
        print("12. Power of Number (reduce and lambda)")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            try:
                n = int(input("Enter a non-negative integer for factorial calculation: "))
                print(f"Factorial of {n} (recursive):", factorial(n))
            except ValueError:
                print("Invalid input. Please enter a non-negative integer.")
        elif choice == '2':
            try:
                n = int(input("Enter a non-negative integer for factorial calculation: "))
                print(f"Factorial of {n} (using reduce and lambda):", factorial_reduce(n))
            except ValueError:
                print("Invalid input. Please enter a non-negative integer.")
        elif choice == '3':
            try:
                n = int(input("Enter a non-negative integer for Fibonacci sequence: "))
                print(f"Fibonacci sequence (first {n} numbers):", fibonacci_list(n))
            except ValueError:
                print("Invalid input. Please enter a non-negative integer.")
        elif choice == '4':
            try:
                n = int(input("Enter a non-negative integer for Fibonacci sequence: "))
                print(f"Fibonacci sequence (first {n} numbers):", fibonacci_list(n))
            except ValueError:
                print("Invalid input. Please enter a non-negative integer.")
        elif choice == '5':
            try:
                n = int(input("Enter an integer to check if it's prime: "))
                print(f"{n} is prime:", is_prime(n))
            except ValueError:
                print("Invalid input. Please enter an integer.")
        elif choice == '6':
            try:
                numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
                print("Prime numbers in the list:", filter_primes(numbers))
            except ValueError:
                print("Invalid input. Please enter a list of numbers.")
        elif choice == '7':
            try:
                numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
                print("Sum of squares:", sum_of_squares(numbers))
            except ValueError:
                print("Invalid input. Please enter a list of numbers.")
        elif choice == '8':
            s = input("Enter a string to reverse: ")
            print("Reversed string (recursive):", reverse_string(s))
        elif choice == '9':
            s = input("Enter a string to reverse words: ")
            print("Reversed words in string:", reverse_words(s))
        elif choice == '10':
            s = input("Enter a string to count words: ")
            print("Number of words:", count_words(s))
        elif choice == '11':
            try:
                x = int(input("Enter the base number: "))
                n = int(input("Enter the exponent (non-negative integer): "))
                print(f"{x}^{n} (recursive):", power(x, n))
            except ValueError:
                print("Invalid input. Please enter integers.")
        elif choice == '12':
            try:
                x = int(input("Enter the base number: "))
                n = int(input("Enter the exponent (non-negative integer): "))
                print(f"{x}^{n} (using reduce and lambda):", power_reduce(x, n))
            except ValueError:
                print("Invalid input. Please enter integers.")
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number from the menu.")


if __name__ == "__main__":
    main()
