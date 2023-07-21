# Import the random module to generate random numbers
import random

# Function to generate a list of 100 random numbers
def generate_random_list():
    return [random.randint(1, 1000) for _ in range(100)]

# Create 10 lists, each containing 100 random numbers
lists = [generate_random_list() for _ in range(10)]

# Print the lists
for i, lst in enumerate(lists, 1):
    print(f"List {i}: {lst}")