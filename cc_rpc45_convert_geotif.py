import scipy.io
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import rasterio
from rasterio.transform import from_origin

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
lat_grid = data['lat_grid']
lon_grid = data['lon_grid']

# Create surface plots and GeoTIFFs for each selected variable
for var in variables:
    if var in data:
        value_grid = data[var]
        
        # Initialize 3D plot
        fig = plt.figure(figsize=(10, 6))
        ax = fig.add_subplot(111, projection='3d')
        
        # Plot the surface
        surf = ax.plot_surface(lon_grid, lat_grid, value_grid, cmap='viridis', edgecolor='k')

        # Label the axes and color bar
        ax.set_xlabel('Longitude')
        ax.set_ylabel('Latitude')
        ax.set_zlabel('Climate Change Projection')
        fig.colorbar(surf, ax=ax, label='')

        # Customize the view angle for a better perspective
        ax.view_init(elev=30, azim=135)

        # Title the plot for clarity
        plt.title(f"Climate Change Surface Plot for {var}")
        plt.show()

        # Generate GeoTIFF file
        # Define the filename for GeoTIFF
        geo_tiff_filename = f"{var}.tif"
        
        # Create a transform for the GeoTIFF (assuming lat/lon grids are equally spaced)
        transform = from_origin(lon_grid[0, 0], lat_grid[0, 0], lon_grid[1, 0] - lon_grid[0, 0], lat_grid[0, 1] - lat_grid[0, 0])
        
        # Write the GeoTIFF file
        with rasterio.open(
            geo_tiff_filename,
            'w',
            driver='GTiff',
            height=value_grid.shape[0],
            width=value_grid.shape[1],
            count=1,
            dtype=value_grid.dtype,
            crs='EPSG:4326',  # Use appropriate CRS
            transform=transform
        ) as dst:
            dst.write(value_grid, 1)  # Write the data to the first band

        print(f"GeoTIFF file '{geo_tiff_filename}' created successfully.")
    else:
        print(f"Variable '{var}' not found in the data.")
