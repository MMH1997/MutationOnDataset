import pandas as pd
import numpy as np
import random

# Define the comma random change function
def random_comma_change(number):
    if len(number) == 1 and number.isdigit():
        return int(number)  # Returns the number as an integer if it is a single digit and a digit

    if '.' not in number:
        number += '.0'
    digits = list(number)
    original_comma_position = digits.index('.')
    digits.pop(original_comma_position)
    possible_positions = [i for i in range(1, len(digits) + 1) if i != original_comma_position]
    new_position = random.choice(possible_positions)
    digits.insert(new_position, '.')
    return float(''.join(digits))  # Converts the result into a floating-point number before returning it

# Define a function to apply the random change function n times in the DataFrame
def apply_random_change(df, n):
    # Find the numeric cells
    numeric_cells = df.select_dtypes(include=[np.number])

    # Check if there are numeric cells
    if numeric_cells.empty:
        print("There are no numeric cells in the DataFrame.")
        return

    num_numeric_cells = numeric_cells.size

    if n > num_numeric_cells:
        raise ValueError("n is greater than the number of numeric cells in the DataFrame")

    # Randomly select n numeric cells
    selected = random.sample(list(numeric_cells.stack().index), n)

    # Apply the random change function to the selected cells
    for index in selected:
        # Print the row and column before applying the change
        print(f"Modified Row: {index[0]}, Modified Column: {index[1]}")
        
        # Apply the change
        df.loc[index] = random_comma_change(str(df.loc[index]))

# Example DataFrame creation:
data = {
    'A': [1, 2, 3, 4],
    'B': [0.5, 0.6, 0.7, 0.8],
    'C': ['a', 'b', 'c', 'd']
}
df = pd.DataFrame(data)

# Example of usage:
try:
    apply_random_change(df, 2)  # Apply the function 2 times
    print(df)
except ValueError as e:
    print(e)
