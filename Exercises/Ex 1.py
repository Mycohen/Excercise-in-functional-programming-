import math
import ast
import string


# Exercise 1.1
def check_correct_triangle():
    print("Enter three numbers: ")
    a = float(input())
    b = float(input())
    c = float(input())
    if (a + b) > c and (a + c) > b and (b + c) > a:
        print("Correct triangle side lengths")
        return True
    else:
        print("Not correct triangle side lengths")
        return False


# Exercise 1.2
def getNumber(param: string):
    print(param)
    return float(input(param))


def calculate_area_and_volume():
    # Define nested functions to calculate area and volume

    def rectangleArea(width, height):
        return width * height

    def circleArea(radius):
        return math.pi * radius ** 2

    def triangleArea(base, height):
        return 0.5 * base * height

    def squareArea(side):
        return side ** 2

    def sphereVolume(radius):
        return (4 / 3) * math.pi * radius ** 3

    def coneVolume(radius, height):
        return (1 / 3) * math.pi * radius ** 2 * height

    def squarePyramidVolume(base_side, height):
        return (1 / 3) * base_side ** 2 * height

    def printMenu(shapes):
        for i, shape in enumerate(shapes, start=1):
            print(f"{i}. {shape}")

    print("Welcome to the Area and Volume calculation program")
    print("------------------------------------------------\n")

    shapes = [
        "Rectangle",
        "Circle",
        "Triangle",
        "Square",
        "Sphere (Volume)",
        "Cone (Volume)",
        "Square Pyramid (Volume)",
        "Quit"
    ]

    while True:
        print("\nPlease select a shape or volume calculation:")
        printMenu(shapes)

        choice = input("> ").strip().lower()

        if choice == "1":
            height = getNumber("Please enter the height of the rectangle: ")
            width = getNumber("Please enter the width of the rectangle: ")
            area = rectangleArea(width, height)
            print(f"The area of the rectangle is: {area}")
        elif choice == "2":
            radius = getNumber("Please enter the radius of the circle: ")
            area = circleArea(radius)
            print(f"The area of the circle is: {area}")
        elif choice == "3":
            base = getNumber("Please enter the base length of the triangle: ")
            height = getNumber("Please enter the height of the triangle: ")
            area = triangleArea(base, height)
            print(f"The area of the triangle is: {area}")
        elif choice == "4":
            side = getNumber("Please enter the side length of the square: ")
            area = squareArea(side)
            print(f"The area of the square is: {area}")
        elif choice == "5":
            radius = getNumber("Please enter the radius of the sphere: ")
            volume = sphereVolume(radius)
            print(f"The volume of the sphere is: {volume}")
        elif choice == "6":
            radius = getNumber("Please enter the radius of the cone's base: ")
            height = getNumber("Please enter the height of the cone: ")
            volume = coneVolume(radius, height)
            print(f"The volume of the cone is: {volume}")
        elif choice == "7":
            base_side = getNumber("Please enter the base side length of the square pyramid: ")
            height = getNumber("Please enter the height of the square pyramid: ")
            volume = squarePyramidVolume(base_side, height)
            print(f"The volume of the square pyramid is: {volume}")
        elif choice in {"quit", "q", "0"}:
            print("Bye!")
            break
        else:
            print("Invalid choice. Please select again.")


#1.3.1
def print_middle_numbers():
    print("Enter 4 numbers: ")
    l=[]
    for i in range(4):
        num = float(input())
        l.append(num)
    l.sort()
    print(f"Middle numbers are: {l[1]} and {l[2]}")

#1.3.2
def print_middle_witout_sort():
    print("Enter 4 numbers: ")
    l=[]
    for i in range(4):
        num = float(input())
        l.append(num)
        for j in range(i, 0, -1):
            if l[j] < l[j - 1]:
                l[j], l[j - 1] = l[j - 1], l[j]
    print(f"Middle numbers are: {l[1]} and {l[2]}")

#1.3.3
def with_sort(mylist: list):
    mylist.sort()  # Sort the list in place
    return mylist  # Return the sorted list

def without_sort(mylist: list):
    size = len(mylist)
    for i in range(size):
        for j in range(i, 0, -1):
            if mylist[j] < mylist[j - 1]:
                mylist[j], mylist[j - 1] = mylist[j - 1], mylist[j]
    return mylist


def print_middle_numbers_with_tuple():
    # Get input from the user
    tuple_str = input("Enter a tuple of numbers: ")

    try:
        # Use ast.literal_eval to safely evaluate the input string as a Python literal
        result_tuple = ast.literal_eval(tuple_str)

        # Check if result_tuple is a tuple
        if isinstance(result_tuple, tuple):
            # Convert tuple_str to a list and sort it
            copy_of_t = list(result_tuple)
            choice = input("Do you want to use  the sort function? (yes/no): ")
            if choice.lower() == "yes":
                copy_of_t = with_sort(copy_of_t)
            else:
                copy_of_t = without_sort(copy_of_t)

            # Print the middle 2 numbers in their size
            middle_index = len(copy_of_t) // 2
            middle_numbers = copy_of_t[middle_index - 1: middle_index + 1]  # Get the middle 2 numbers
            print(f"Middle numbers in their size: {middle_numbers[0]} and {middle_numbers[1]}")
        else:
            print("Input is not a valid tuple of numbers.")

    except ValueError:
        print("Invalid input. Please enter a valid tuple of numbers.")




