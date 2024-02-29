import pandas as pd
import numpy as np

def sign_change(df, n):
    """
    Applies random transformation to n numerical elements of the DataFrame.

    Parameters:
    - df: pandas DataFrame.
    - n: Number of elements to transform.

    Returns:
    - DataFrame with transformed elements.
    """
    # Get a list of numeric columns of the DataFrame
    numeric_columns = df.select_dtypes(include=np.number).columns.tolist()
    
    # Randomly select n elements from the DataFrame
    selected_indices = np.random.choice(df.index, n, replace=False)
    
    for index in selected_indices:
        # Randomly select a numeric column from the DataFrame
        column = np.random.choice(numeric_columns)
        
        # Apply transformation to the selected element
        df.loc[index, column] = -df.loc[index, column]
        
        # Print the modified row and column
        print(f"Modified Row: {index}, Modified Column: {column}")
    
    return df
