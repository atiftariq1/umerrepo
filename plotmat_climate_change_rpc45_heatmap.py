import scipy.io
import numpy as np
import matplotlib.pyplot as plt

# Load the .mat file with climate change data
data = scipy.io.loadmat('data.mat')  # Replace with the actual filename

# Define the specific RCP 4.5 variables for different seasons and time periods
variables = [
    'cc_DJF_rcp45_2021_2040', 'cc_DJF_rcp45_2041_2060', 'cc_DJF_rcp45_2061_2080', 'cc_DJF_rcp45_2081_2100',
    'cc_JJA_rcp45_2021_2040', 'cc_JJA_rcp45_2041_2060', 'cc_JJA_rcp45_2061_2080', 'cc_JJA_rcp45_2081_2100',
    'cc_MAM_rcp45_2021_2040', 'cc_MAM_rcp45_2041_2060', 'cc_MAM_rcp45_2061_2080', 'cc_MAM_rcp45_2081_2100',
    'cc_SON_rcp45_2021_2040'
]

# Load latitude and longitude grids (assuming they are the same across all projections)
lat_grid = data['lat_grid'].flatten()  # Ensure it is a 1D array for heatmap
lon_grid = data['lon_grid'].flatten()  # Ensure it is a 1D array for heatmap

# Create heatmaps for each selected variable
for var in variables:
    if var in data:
        value_grid = data[var]

        # Create a heatmap
        plt.figure(figsize=(10, 6))
        plt.imshow(value_grid, aspect='auto', cmap='viridis', extent=[lon_grid.min(), lon_grid.max(), lat_grid.min(), lat_grid.max()])
        
        # Add labels and color bar
        plt.colorbar(label='Climate Change Projection')
        plt.xlabel('Longitude')
        plt.ylabel('Latitude')

        # Title the plot for clarity
        plt.title(f"Climate Change Heatmap for {var}")
        plt.show()
    else:
        print(f"Variable '{var}' not found in the data.")
