#Exercise 2 in Functional programming
#Moshe Yaakov Cohen 324692680
#Question 1

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



functionalPentaRange()





