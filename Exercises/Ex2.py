#Exercise 2 in Functional programming
#Moshe Yaakov Cohen 324692680
#Question 1
from functools import reduce


#1.1
def pentaNumRange(n1, n2):
    getPentalNum = lambda n: n * (3 * n - 1) // 2
    return list(map(getPentalNum,range(n1,n2)))

#1.2
def nonFuncPenta():
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
#1.3
def  checkNumbers(n1, n2):
    return  n2>= 0 and n1>=0 and n2 > n1

def functionalPenta(n1, n2):
    return list(map(lambda n:n * (3 * n - 1) // 2, range(n1,n2)))

def recursivePrint(myList):
    if len(myList)<=10:
        print (myList)
        return
    print (myList[:10])
    recursivePrint(myList[10:])
    return

def functionalPentaRange():
    n1 = int(input("Enter the value of n1: "))
    n2 = int(input("Enter the value of n2: "))
    if not checkNumbers(n1,n2):
        print("ERROR: the values must be positive integers and n2 > n1")
        return
    else:
        myList = functionalPenta(n1, n2)
        recursivePrint(myList)



#2.1
def sumDigits(n: int):
    return sum(splitDigits(n))



def splitDigits(n: int):
    return list(map(int, str(abs(n))))

#2.2
def applySum():
    print("Enter an integer number n (positive or negative):")
    try:

        n = int(input())
        print(sumDigits(n))
    except ValueError:
        print("ERROR: Input number is incorrect!")

#2.3
def reverseNumber(n:int):
    return str(abs(n))[::-1]

#3.1
def isPalindrum(n: int):
    return reverseNumber(n) == str(abs(n))
#3.2
def isPalindrome():
    print("Enter an integer number n (positive or negative):")
    try:
        n = int(input())
        if isPalindrum(n):
            print("It is a palindrome")
        else:
            print("It is not a palindrome")
    except ValueError:
        print("ERROR: Input number is incorrect!")

#4.1
def m(i):
    if i == 1:
        return -0.5
    return i / (i + 1)

def my(n):
    return list(map(lambda x: (m(x) + 1), range(1, n + 1)))

def anotherRecursivePrint(param, n=1):
    if len(param) == 1:
        print(f"{n} {param[0]}")
    else:
        print(f"{n} {param[0]}")
        anotherRecursivePrint(param[1:], n + 1)
#4.2
def process_number():
    print("Enter a natural number:")
    try:
        n = int(input())
        if n <= 0:
            raise ValueError()
        anotherRecursivePrint(my(n))
    except ValueError:
        print("ERROR: Input number is incorrect!")

#5.1
def add3dicts(d1, d2, d3):
    # This function combines keys from three dictionaries into a set
    # and passes them to a helper function to create the merged dictionary.
    d4 = set()
    d4.update(d1)  # Add keys from d1 to d4
    d4.update(d2)  # Add keys from d2 to d4
    d4.update(d3)  # Add keys from d3 to d4
    return helper(d1, d2, d3, d4)

def helper(d1, d2, d3, d4):
    # This helper function recursively processes the set of keys (d4)
    # and creates a list of tuples (key, (values,)) where values are
    # combined from the three dictionaries for each key.
    if len(d4) == 0:
        return []
    else:
        key = d4.pop()  # Remove and return an arbitrary key from d4
        temp = set()  # Temporary set to store unique values for the key
        if d1.setdefault(key) is not None:
            temp.add(d1[key])
        if d2.setdefault(key) is not None:
            temp.add(d2[key])
        if d3.setdefault(key) is not None:
            temp.add(d3[key])
        return [(key, tuple(temp))] + helper(d1, d2, d3, d4)

def test_add3dicts():
    # This function tests the add3dicts function by taking user input for
    # three dictionaries, validating the input, and printing the merged result.
    d1 = eval(input("Enter a dictionary: "))
    d2 = eval(input("Enter a dictionary: "))
    d3 = eval(input("Enter a dictionary: "))
    if type(d1) != dict or type(d2) != dict or type(d3) != dict:
        print("ERROR: Input is incorrect!")
        return
    print(dict(add3dicts(d1, d2, d3)))
    return
