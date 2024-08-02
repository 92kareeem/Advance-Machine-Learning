import pandas as pd

# Generate XOR dataset
data = {
    'Input1': [0, 0, 1, 1],
    'Input2': [0, 1, 0, 1],
    'Output': [0, 1, 1, 0]
}

# Create a DataFrame
xor_data = pd.DataFrame(data)

# Save to CSV file
xor_data.to_csv('xor_data.csv', index=False)

# Display the DataFrame
print(xor_data)
