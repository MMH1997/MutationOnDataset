import pandas as pd
import random

def modify_dataframe_randomly(df, n):
    """
    Randomly modifies "n" distinct numeric elements of the DataFrame df.

    Args:
    - df: pandas DataFrame.
    - n: Exact number of elements to modify.

    Returns:
    - Modified DataFrame.
    """
    def modify_numeric_cell(cell_value):
        """
        Internal function to randomly modify a numeric cell.
        """
        # Convert cell value to integer
        cell_value_int = int(cell_value)
        
        # Convert cell value to a list of digits
        digits = [int(d) for d in str(abs(cell_value_int))]
        
        # Get the number of digits
        num_digits = len(digits)
        
        # Randomly choose a digit to modify
        digit_index_to_modify = random.randint(0, num_digits - 1)
        
        # Generate a new random digit different from the current digit
        new_digit = random.randint(0, 9)
        while new_digit == digits[digit_index_to_modify]:
            new_digit = random.randint(0, 9)
        
        # Modify the digit in the list of digits
        digits[digit_index_to_modify] = new_digit
        
        # Reconstruct the new value as an integer
        new_value = int(''.join(map(str, digits)))
        
        # Maintain the sign of the original value
        if cell_value_int < 0:
            new_value = -new_value
        
        return new_value

    # Get a list of unique numeric cells
    numeric_cells = [(row, col) for row in df.index for col in df.columns if pd.api.types.is_numeric_dtype(df.loc[row, col])]

    # Check that "n" does not exceed the number of numeric cells
    if n > len(numeric_cells):
        raise ValueError("The number of elements to modify ('n') cannot be greater than the number of numeric cells in the DataFrame.")

    # Randomly select "n" unique cells to modify
    random_cells = random.sample(numeric_cells, n)

    # Apply the modification function to the selected cells
    for row, col in random_cells:
        # Print the row and column before applying the change
        print(f"Modified Row: {row}, Modified Column: {col}")
        
        # Get the current value of the cell
        current_value = df.loc[row, col]
        
        # Modify the cell value by calling the internal function
        df.loc[row, col] = modify_numeric_cell(current_value)

    return df

# Example of usage
data = {'A': [123.4, -456.8, 789],
        'B': [234.6, 567, -890.1],
        'C': [-345.9, 678, 901.7]}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

try:
    # Randomly modify the DataFrame
    modify_dataframe_randomly(df, 2)
    print("\nModified DataFrame:")
    print(df)
except ValueError as error:
    print(error)
