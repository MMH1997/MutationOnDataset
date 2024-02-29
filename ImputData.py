import pandas as pd
import numpy as np
import random

def replace_cells_with_previous(df, n):
    # Select numeric columns
    numeric_columns = df.select_dtypes(include=[np.number])

    # Get a list of numeric cells that are not the first of their column
    non_first_cells = [(i, column) for column in numeric_columns.columns for i in range(1, len(df))]

    if n > len(non_first_cells):
        raise ValueError("n is greater than the number of cells that can be selected in the DataFrame")

    # Randomly select n cells from the list
    selected = random.sample(non_first_cells, n)

    # Replace the value of the selected cells with the previous value
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
    replace_cells_with_previous(df, 2)  # Attempt to replace 2 cells with the previous value
    print("\nDataFrame with cells replaced by the previous value:")
    print(df)
except ValueError as e:
    print(e)
