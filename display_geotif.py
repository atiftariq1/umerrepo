import rasterio
import matplotlib.pyplot as plt
import numpy as np

# Define the path to the GeoTIFF file
geo_tiff_path = r"/umer\raster_data\cc_DJF_rcp45_2021_2040.tif"  # Change this to your GeoTIFF file path

# Open the GeoTIFF file
with rasterio.open(geo_tiff_path) as src:
    # Read the data from the first band
    band1 = src.read(1)
    
    # Get the extent for plotting
    extent = [src.bounds.left, src.bounds.right, src.bounds.bottom, src.bounds.top]

# Plotting
plt.figure(figsize=(10, 6))
plt.imshow(band1, extent=extent, cmap='viridis', origin='upper')
plt.colorbar(label='Climate Change Variable Value')
plt.title('Climate Change Data - GeoTIFF Visualization')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.grid(True)
plt.show()
