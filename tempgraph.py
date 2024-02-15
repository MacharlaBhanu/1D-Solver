import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
data = pd.read_csv('Diploma-Thesis---Inverse-Heat-Transfer/DATA.csv')  # Replace 'data.csv' with your file name

# Extract columns for plotting
x = data['Time']  # Replace 'x_column_name' with the actual column name
y = data['Temperature']  # Replace 'y_column_name' with the actual column name

# Plot the data
plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
plt.plot(x, y, marker='.', linestyle=' ',linewidth=0.001, color='r')

plt.title('Experimenttal data')
plt.xlabel('Time')
plt.ylabel('Temperature')
plt.grid(True)
plt.show()