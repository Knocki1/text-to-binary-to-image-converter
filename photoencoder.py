import cv2
import numpy as np


inputfile=input("Enter the location of file")
# Read the text file
with open(inputfile, 'r') as f:
    data = f.read()

# Convert the text to binary
binary = ''.join(format(ord(i), '08b') for i in data)

# Create an array of 0s and 1s
arr = np.array([int(i) for i in binary])

# Reshape the array to a square matrix
n = int(np.ceil(np.sqrt(len(arr))))
arr.resize((n, n))

# Scale the matrix to 255
arr *= 255

# Create a black and white image from the matrix
img = np.zeros((n, n), dtype=np.uint8)
img[arr > 0] = 255

# Save the image
cv2.imwrite('output.png', img)




#limitation will be required for the data till 2800 bits