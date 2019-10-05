import sys
import pandas as pd

input_file = "supplier_data.csv"
output_file = "pandas_output_data.csv"

data_frame = pd.read_csv(input_file)
print(data_frame)
data_frame.to_csv(output_file)