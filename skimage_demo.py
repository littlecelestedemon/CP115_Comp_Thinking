import skimage
import os

from skimage import io
from skimage import color

import matplotlib.pyplot as plt


# drags an image from my desktop and displays it
img = io.imread("/Users/willapolman/Desktop/Drowning.jpg")
plt.imshow(img)
plt.show()

# converts the image on my deskstop into a strange neon look
new_image = skimage.color.rgb2gray(img)
plt.imshow(new_image)
plt.show()

# saves the new picture back to the desktop with the name new.jpg
skimage.io.imsave(fname = "new.jpg", arr = new_image)
