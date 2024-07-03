import math
import random
import string
import re

# Function to check if three numbers can form a triangle
def check_correct_triangle_qustion_1():
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

# Function to get a float number input with a prompt message
def getNumber(param: string):
    return float(input(param))

# Function to calculate area and volume based on user selection
def calculate_area_and_volume_question_2():
    # Nested functions for calculating area and volume of different shapes
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
        # Function to print menu options
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

        # Handle user choices for different shapes or quitting
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

# Function to sort a list using built-in sort method
def with_sort(mylist: list):
    mylist.sort()  # Sort the list in place
    return mylist  # Return the sorted list

# Function to sort a list without using built-in sort method
def without_sort(mylist: list):
    size = len(mylist)
    for i in range(size):
        for j in range(i, 0, -1):
            if mylist[j] < mylist[j - 1]:
                mylist[j], mylist[j - 1] = mylist[j - 1], mylist[j]
    return mylist

# Function to extract all numbers from nested structures (lists, tuples)
def extract_numbers(data):
    numbers = []
    if isinstance(data, (int, float)):
        numbers.append(data)
    elif isinstance(data, (list, tuple)):
        for item in data:
            numbers.extend(extract_numbers(item))
    return numbers

# Function to parse input string into a tuple of numbers
def parse_input(input_str):
    try:
        numbers = re.findall(r'-?\d+\.?\d*', input_str)
        numbers = [int(num) if '.' not in num else float(num) for num in numbers]
        return tuple(numbers)
    except (ValueError, SyntaxError):
        raise ValueError("Input string is not a valid tuple of numbers")

# Function to handle tuple operations: sorting and finding middle elements
def convert_check_and_sub_menu(tuple_str: str):
    result_tuple = parse_input(tuple_str)
    copy_of_t = list(result_tuple)
    choice = input("Do you want to use the sort built-in function? (yes/no) ")
    if choice.lower() == "yes":
        copy_of_t = with_sort(copy_of_t)
    else:
        copy_of_t = without_sort(copy_of_t)
    return copy_of_t

# Function for question 3: operating on tuples of numbers
def question_3():
    try:
        choice = input("Which section do you want to run? (1-3) ")
        if choice in ["1", "2", "3"]:
            tuple_stri = input("Enter a tuple with numbers: ")
            if choice == "1":
                if len(parse_input(tuple_stri)) != 4:
                    print("Invalid input. Please enter a valid tuple of four numbers.")
                    return
                copy_of_t = convert_check_and_sub_menu(tuple_stri)
            elif choice == "2":
                copy_of_t = convert_check_and_sub_menu(tuple_stri)
            elif choice == "3":
                copy_of_t = list(parse_input(tuple_stri))
            middle_index = len(copy_of_t) // 2
            middle_numbers = copy_of_t[middle_index - 1: middle_index + 1]
            print(f"Middle numbers in their size: {middle_numbers[0]} and {middle_numbers[1]}")
        else:
            print("Invalid choice. Please select a section (1-3).")
    except (ValueError, SyntaxError) as e:
        print(f"Invalid input. {e}")

# Function to perform left shift operation on a binary number
def shiftL(binNr, N):
    return '0' * N + binNr[:-N]

# Function to perform right shift operation on a binary number
def shiftR(binNr, N):
    return binNr[N:] + '0' * N

# Function to perform circular left shift operation on a binary number
def shiftCL(binNr, N):
    return binNr[N:] + binNr[:N]

# Function to perform circular right shift operation on a binary number
def shiftCR(binNr, N):
    return binNr[-N:] + binNr[:-N]

# Function for question 4: binary shifting operations
def question_4():
    while True:
        print("Binary Shifting Menu:")
        print("1. Shift Left (shiftL)")
        print("2. Shift Right (shiftR)")
        print("3. Circular Left Shift (shiftCL)")
        print("4. Circular Right Shift (shiftCR)")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        # Perform the selected binary shifting operation
        if choice == "1":
            binNr = input("Enter the binary number: ")
            N = int(input("Enter the number of places to shift: "))
            result = shiftL(binNr, N)
            print(f"Result of shiftL({binNr}, {N}): {result}")
        elif choice == "2":
            binNr = input("Enter the binary number: ")
            N = int(input("Enter the number of places to shift: "))
            result = shiftR(binNr, N)
            print(f"Result of shiftR({binNr}, {N}): {result}")
        elif choice == "3":
            binNr = input("Enter the binary number: ")
            N = int(input("Enter the number of places to shift: "))
            result = shiftCL(binNr, N)
            print(f"Result of shiftCL({binNr}, {N}): {result}")
        elif choice == "4":
            binNr = input("Enter the binary number: ")
            N = int(input("Enter the number of places to shift: "))
            result = shiftCR(binNr, N)
            print(f"Result of shiftCR({binNr}, {N}): {result}")
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

# Function to count types (int, str, tuple, list) in a given list
def count_types_question_5(input_list):
    type_counts = {
        'int': 0,
        'str': 0,
        'tuple': 0,
        'list': 0
    }

    for item in input_list:
        if isinstance(item, int):
            type_counts['int'] += 1
        elif isinstance(item, str):
            type_counts['str'] += 1
        elif isinstance(item, tuple):
            type_counts['tuple'] += 1
        elif isinstance(item, list):
            type_counts['list'] += 1

    return type_counts

# Function to create a random tuple of N integers between 1 and 9
def create_random_record(N):
    return tuple(random.randint(1, 9) for _ in range(N))

# Function to perform a number guessing game with success rate tracking
def nihushTest(random_record, *guesses):
    result = []
    for idx, guess in enumerate(guesses):
        if guess == random_record[idx]:
            result.append(guess)
        else:
            result.append("X")
    return tuple(result)

# Function for question 6: number guessing game
def play_game_question_6():
    random.seed()
    N = random.randint(3, 9)
    random_record = create_random_record(N)
    max_success_rate = 0

    while True:
        guess_str = input(f"Guess the {N} numbers (separated by spaces): ")
        guesses = tuple(map(int, guess_str.split()))

        if len(guesses) != N:
            print(f"Please enter exactly {N} numbers.")
            continue

        result = nihushTest(random_record, *guesses)
        print(f"Result: {result}")

        success_rate = result.count('X') / N
        print(f"Success rate: {100 * (1 - success_rate):.2f}%")

        if success_rate == 0:
            print("Perfect guess!")
            break

        if success_rate > max_success_rate:
            max_success_rate = success_rate

        play_again = input("Play again? (yes/no): ").lower()
        if play_again != "yes":
            break

    print(f"Random record chosen: {random_record}")
    print(f"Highest success rate achieved: {100 * max_success_rate:.2f}%")

# Main function to present a menu for all questions and execute user's choice
def main():
    funcs = [
        check_correct_triangle_qustion_1,
        calculate_area_and_volume_question_2,
        question_3,
        question_4,
        count_types_question_5,
        play_game_question_6
    ]
    descriptions = [
        "Check if three numbers can form a triangle",
        "Calculate area or volume based on user selection",
        "Operate on tuples of numbers: sorting and middle elements",
        "Binary shifting operations",
        "Count types (int, str, tuple, list) in a given list",
        "Number guessing game with success rate tracking"
    ]

    while True:
        print("\nYour choices:")
        for i, desc in enumerate(descriptions):
            print(f"{i + 1}. {desc}")
        print("0. Exit")

        try:
            choice = int(input("Please enter your choice: "))
            if choice == 0:
                print("Exiting...")
                break
            elif choice >= 1 and choice <= len(funcs):
                funcs[choice - 1]()
            else:
                print("Invalid choice. Please enter a number between 0 and", len(funcs))
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
