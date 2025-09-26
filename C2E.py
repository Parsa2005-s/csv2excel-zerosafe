import pandas as pd
import os
from io import StringIO

def convert_csv_to_excel_with_leading_zeros(csv_data, excel_file_path):
    """
    Reads data from a CSV-formatted string, converts it to an Excel file,
    and ensures that leading zeros in the data are preserved.

    Args:
        csv_data (str): A string containing the data in CSV format.
        excel_file_path (str): The path where the output Excel file will be saved.
    """
    try:
        # --- The Key Step ---
        # Use StringIO to treat the csv_data string as a file.
        # Then, read the "file" and treat all columns as strings ('str').
        # This is crucial for preserving leading zeros.
        print("Reading data from the string...")
        df = pd.read_csv(StringIO(csv_data), dtype=str)

        # Fill any potential empty cells (NaN) with an empty string
        df.fillna('', inplace=True)

        # Write the DataFrame to an Excel file.
        # The 'index=False' argument prevents pandas from writing the
        # DataFrame index (row numbers) into the Excel sheet.
        # The 'engine='openpyxl'' argument specifies the library to use for writing.
        print(f"Writing data to '{excel_file_path}'...")
        df.to_excel(excel_file_path, index=False, engine='openpyxl')

        print("\nConversion successful!")
        print(f"File saved at: {os.path.abspath(excel_file_path)}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# --- How to Use ---
if __name__ == "__main__":
    # 1. Manually enter your data here in CSV format inside the triple quotes.
    #    The first line should be your headers.
    manual_csv_data = """
    
    
    
"""

    # 2. Define the output file name.
    output_excel = 'output_with_leading_zeros.xlsx'

    # 3. Call the function to perform the conversion.
    convert_csv_to_excel_with_leading_zeros(manual_csv_data, output_excel)


