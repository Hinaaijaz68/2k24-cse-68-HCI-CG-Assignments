import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Load the image
image = Image.open("sample.jpg").convert("RGB")

# Convert image to NumPy array
img = np.array(image)

# Extract Red, Green, and Blue channels
red_channel = img[:, :, 0]
green_channel = img[:, :, 1]
blue_channel = img[:, :, 2]

# Print channel information
print("\n--- CHANNEL EXTRACTION SUMMARY ---")
print(f"Original Image Shape  : {img.shape}")

print(
    f"Red Channel 2D Shape  : {red_channel.shape} | "
    f"Mean Intensity: {red_channel.mean():.2f}"
)

print(
    f"Green Channel 2D Shape: {green_channel.shape} | "
    f"Mean Intensity: {green_channel.mean():.2f}"
)

print(
    f"Blue Channel 2D Shape : {blue_channel.shape} | "
    f"Mean Intensity: {blue_channel.mean():.2f}"
)

# Create separate color images
red_only = np.zeros_like(img)
green_only = np.zeros_like(img)
blue_only = np.zeros_like(img)

# Keep only one channel active
red_only[:, :, 0] = red_channel
green_only[:, :, 1] = green_channel
blue_only[:, :, 2] = blue_channel

# Create 2 x 3 subplot
fig, axes = plt.subplots(2, 3, figsize=(15, 8))

# Top row: Color-only images
axes[0, 0].imshow(red_only)
axes[0, 0].set_title("Red-Only")

axes[0, 1].imshow(green_only)
axes[0, 1].set_title("Green-Only")

axes[0, 2].imshow(blue_only)
axes[0, 2].set_title("Blue-Only")

# Bottom row: Grayscale intensity maps
axes[1, 0].imshow(red_channel, cmap="gray")
axes[1, 0].set_title("Red Channel - Grayscale")

axes[1, 1].imshow(green_channel, cmap="gray")
axes[1, 1].set_title("Green Channel - Grayscale")

axes[1, 2].imshow(blue_channel, cmap="gray")
axes[1, 2].set_title("Blue Channel - Grayscale")

# Remove axes
for ax in axes.flat:
    ax.axis("off")

plt.tight_layout()

# Save the figure
plt.savefig("task3_output.png", dpi=300)

print("\nMatplotlib 2x3 Subplot Grid Rendered.")
print("Output saved as: task3_output.png")

plt.show()