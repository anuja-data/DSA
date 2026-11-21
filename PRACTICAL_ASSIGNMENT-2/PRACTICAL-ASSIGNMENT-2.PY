# Q1. Function Scope and Built-in Functions

def analyze_numbers():
    numbers = [15, 78, 96, 87, 65]

    # Find the largest and smallest numbers
    print("Maximum:", max(numbers))
    print("Minimum:", min(numbers))

    # Calculate total and average
    print("Sum:", sum(numbers))
    print("Average:", sum(numbers) / len(numbers))

analyze_numbers()


# Q2. Lambda Function

# Lambda function to calculate square
square = lambda x: x * x

num = int(input("Enter a number: "))
print("Square:", square(num))


# Q3. Math and Random Module

import random
import math

# Generate a random number between 1 and 100
num = random.randint(1, 100)

print("Random Number:", num)

# Find the square root of the number
print("Square Root:", math.sqrt(num))


# Q4. Employee Salary Calculator

def calculate_salary(basic_salary, bonus=2000):

    # Add basic salary and bonus
    return basic_salary + bonus

# Using default argument
print("Employee 1 Salary:", calculate_salary(30000))

# Using keyword argument
print("Employee 2 Salary:", calculate_salary(basic_salary=33000))

# Using positional argument
print("Employee 3 Salary:", calculate_salary(25000, 2000))


# Q5. Map, Filter and Reduce

from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Map is used to find the square of each number
squares = list(map(lambda x: x*x, numbers))

# Filter is used to get only even numbers
even = list(filter(lambda x: x % 2 == 0, numbers))

# Reduce is used to calculate the total sum
total = reduce(lambda x, y: x+y, numbers)

print("Squares:", squares)
print("Even Numbers:", even)
print("Sum:", total)


# Q7. Generator and Datetime Module

from datetime import date, timedelta

def generate_dates():

    # Get today's date
    today = date.today()

    # Generate dates for the next 7 days
    for i in range(7):
        yield today + timedelta(days=i)

# Display all generated dates
for d in generate_dates():
    print(d)