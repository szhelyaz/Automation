# Create a list of even numbers from 1 to 20
even_numbers = [x for x in range(1, 21) if x % 2 == 0]

# Remove numbers divisible by 5
divisible_numbers = [num for num in even_numbers if num % 5 != 0]

# Print the numbers divisible by 5
print(f'Original list , {even_numbers} Otput {divisible_numbers}')
