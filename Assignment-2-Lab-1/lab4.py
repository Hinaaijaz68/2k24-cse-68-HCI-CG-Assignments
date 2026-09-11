import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Load the image
image = Image.open("sample.jpg").convert("RGB")

# Convert image to NumPy array
img = np.array(image)

# Downsampling factor
N = 8

# Downsample the image
downsampled = img[::N, ::N, :]

# Re-expand the image using np.repeat
expanded = np.repeat(
    np.repeat(downsampled, N, axis=0),
    N,
    axis=1
)

# Crop expanded image to original dimensions
expanded = expanded[:img.shape[0], :img.shape[1], :]

# Calculate spatial dimension reduction
height_reduction = (1 - downsampled.shape[0] / img.shape[0]) * 100
width_reduction = (1 - downsampled.shape[1] / img.shape[1]) * 100

# Calculate memory savings
original_memory = img.nbytes
downsampled_memory = downsampled.nbytes
memory_savings = (1 - downsampled_memory / original_memory) * 100

# Print results
print("\n--- DOWNSAMPLING ANALYSIS ---")
print(f"Original Shape       : {img.shape}")
print(f"Downsampled Shape    : {downsampled.shape}")
print(f"Re-expanded Shape    : {expanded.shape}")

print(f"\nOriginal Memory      : {original_memory:,} bytes")
print(f"Downsampled Memory   : {downsampled_memory:,} bytes")

print(f"\nHeight Reduction     : {height_reduction:.2f}%")
print(f"Width Reduction      : {width_reduction:.2f}%")
print(f"Memory Savings       : {memory_savings:.2f}%")

# Display images
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

axes[0].imshow(img)
axes[0].set_title("Original Image")

axes[1].imshow(downsampled)
axes[1].set_title("Downsampled (N=8)")

axes[2].imshow(expanded)
axes[2].set_title("Re-expanded Image")

# Remove axes
for ax in axes:
    ax.axis("off")

plt.tight_layout()

# Save output
plt.savefig("task4_output.png", dpi=300)

print("\nOutput saved as: task4_output.png")

plt.show()