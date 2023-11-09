import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image

# Assuming you have your image and bounding box coordinates
img_path = "Dataset/Test/000016_01_01_030.png"
bbox = [99.8889, 302.556, 151.667, 355.222]

# Open the image
img = Image.open(img_path)

# Create figure and axes
fig, ax = plt.subplots(1)

# Display the image
ax.imshow(img)

# Create a Rectangle patch
rect = patches.Rectangle((bbox[0], bbox[1]), bbox[2] - bbox[0], bbox[3] - bbox[1], linewidth=2, edgecolor='r', facecolor='none')

# Add the rectangle to the Axes
ax.add_patch(rect)

# Show the plot
plt.show()