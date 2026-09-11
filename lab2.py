import numpy as np
import matplotlib.pyplot as plt

# Create a 300 x 400 x 3 image array
img = np.zeros((300, 400, 3), dtype=np.uint8)

# Top-left quadrant: Red
img[:150, :200] = [255, 0, 0]

# Top-right quadrant: Green
img[:150, 200:] = [0, 255, 0]

# Bottom-left quadrant: Blue
img[150:, :200] = [0, 0, 255]

# Bottom-right quadrant: White
img[150:, 200:] = [255, 255, 255]

# Display matrix information
print("\n--- SYNTHETIC MATRIX METRICS ---")
print(f"Array Shape (H, W, C) : {img.shape}")
print(f"Data Type              : {img.dtype}")
print(f"Total Elements         : {img.size:,} values")
print(f"Memory Footprint       : {img.nbytes:,} bytes")
print(f"Memory                  : {img.nbytes / 1024:.2f} KB")

# Display the image
plt.imshow(img)
plt.title("Synthetic 300 x 400 RGB Image")
plt.axis("off")
plt.show()