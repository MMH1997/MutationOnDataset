import pandas as pd
import numpy as np
import random

def replace_cells_with_zero(df, n):
    # Find numeric cells
    numeric_cells = df.select_dtypes(include=[np.number])
    num_numeric_cells = numeric_cells.size

    if n > num_numeric_cells:
        raise ValueError("n is greater than the number of numeric cells in the DataFrame")
    selected_indices = random.sample(list(numeric_cells.stack().index), n)

    # Replace the value of selected cells with 0
    for index in selected_indices:
        row, column = index
        print(f"Modified Row: {row}, Modified Column: {column}")
        df.loc[index] = 0

# Example usage:
data = {
    'A': [1, 2, 3, 4],
    'B': [0.5, 0.6, 0.7, 0.8],
    'C': ['a', 'b', 'c', 'd']
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

try:
    replace_cells_with_zero(df, 2)  # Try to replace 2 cells with 0
    print("\nDataFrame with cells replaced by 0:")
    print(df)
except ValueError as e:
    print(e)
##############################################################


def replace_cells_with_previous(df, n):
    # Select numeric columns
    numeric_columns = df.select_dtypes(include=[np.number])

    # Get a list of numeric cells excluding the first row of each column
    numeric_cells = [(i, j) for i in range(1, len(df)) for j in numeric_columns.columns]

    if n > len(numeric_cells):
        raise ValueError("n is greater than the number of cells that can be selected in the DataFrame")

    # Randomly select n cells from the list
    selected = random.sample(numeric_cells, n)

    # Replace the value of selected cells with the value from the cell above
    for index in selected:
        row, column = index
        print(f"Modified Row: {row}, Modified Column: {column}")
        previous_value = df.iloc[row - 1][column]
        df.at[index] = previous_value

# Example usage:
data = {
    'A': [1, 2, 3, 4],
    'B': [5, 6, 7, 8],
    'C': [9, 10, 11, 12]
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

try:
    replace_cells_with_previous(df, 2)  # Try to replace 2 cells with the previous value
    print("\nDataFrame with cells replaced by the previous value:")
    print(df)
except ValueError as e:
    print(e)
##############################################################


def replace_cells_with_previous_mean(df, n):
    # Select numeric columns
    numeric_columns = df.select_dtypes(include=[np.number])

    # Get a list of numeric cells excluding the first row of each column
    numeric_cells = [(i, column) for column in numeric_columns.columns for i in range(1, len(df))]

    if n > len(numeric_cells):
        raise ValueError("n is greater than the number of cells that can be selected in the DataFrame")

    # Randomly select n cells from the list
    selected = random.sample(numeric_cells, n)

    # Replace the value of selected cells with the mean of previous values in the column, rounded to two decimal places
    for index in selected:
        row, column = index
        print(f"Modified Row: {row}, Modified Column: {column}")
        previous_mean = round(df.iloc[:row][column].mean(), 2)
        df.at[index] = previous_mean

# Example usage:
data = {
    'A': [1, 2, 3, 4],
    'B': [5, 6, 7, 8],
    'C': [9, 10, 11, 12]
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

try:
    replace_cells_with_previous_mean(df, 2)  # Try to replace 2 cells with the previous mean
    print("\nDataFrame with cells replaced by the previous mean:")
    print(df)
except ValueError as e:
    print(e)
#############################################################


def randomly_replace(df, n):
    # List of function names and function references
    functions = [
        ("replace_cells_with_previous_mean", replace_cells_with_previous_mean),
        ("replace_cells_with_previous", replace_cells_with_previous),
        ("replace_cells_with_zero", replace_cells_with_zero)
    ]

    # Repeat the process 'n' times
    for _ in range(n):
        # Randomly select a function
        function_name, function = random.choice(functions)
        try:
            # Apply the selected function to the DataFrame
            function(df, 1)
            print(f"{function_name} applied.")
        except ValueError as e:
            print(e)

# # Example usage:
# data = {
#     'A': [1, 2, 3, 4],
#     'B': [5, 6, 7, 8],
#     'C': [9, 10, 11, 12]
# }
# df = pd.DataFrame(data)

# print("Original DataFrame:")
# print(df)

# # Apply randomly one of the three functions to 3 elements of the DataFrame
# print("\nApply randomly one of the three functions to 3 elements of the DataFrame:")
# randomly_replace(df, 3)
# print(df)
