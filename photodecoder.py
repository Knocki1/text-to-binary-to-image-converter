import cv2

# Read the image
img = cv2.imread('output.png', cv2.IMREAD_GRAYSCALE)

# Convert the image to binary
binary = ''.join(str(int(i)) for i in (img > 0).flatten())

# Convert the binary to text
data = ''.join(chr(int(binary[i:i+8], 2)) for i in range(0, len(binary), 8))


print(data)