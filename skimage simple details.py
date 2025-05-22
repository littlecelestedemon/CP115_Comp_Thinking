import skimage
from skimage.io import imread
from skimage.io import imsave
from skimage.transform import rotate

filename = "/Users/willapolman/Desktop/Drowning.jpg"

# reading the filename
im = imread(filename)

# prints the information of im
print(im)

# rotates it
rotated_im = rotate(im, 45)

# supposed to make a new file and then rotating is
new_filename = "/Users/willapolman/Desktop/Drowning.jpg"
imsave(new_filename, rotated_im)
