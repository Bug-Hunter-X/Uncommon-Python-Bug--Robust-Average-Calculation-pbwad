def calculate_average(numbers):
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0  # Handle case with no numeric values
    return sum(numeric_numbers) / len(numeric_numbers)

# Example usage:
my_numbers = [1, 2, 3, 4, 5]
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_numbers = []
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_numbers = [1,2,3,4,'a']
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_numbers = ['a','b','c']
average = calculate_average(my_numbers)
print(f"The average is: {average}")
