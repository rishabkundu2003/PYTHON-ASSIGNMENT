# Example input
numbers = [4, 7, 10, 13, 8, 9, 2, 5, 6]

expected_even = True    # Start expecting an even number
accepted = []

for num in numbers:
    if expected_even and num % 2 == 0:
        accepted.append(num)
        expected_even = False   # Next expect odd
    elif not expected_even and num % 2 == 1:
        accepted.append(num)
        expected_even = True    # Next expect even

print(accepted)
