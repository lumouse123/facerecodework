import cv2
import os

# Image path
image_path = r'a1.jpg'

# to read the image
img = cv2.imread(image_path)


# List files and directories  
# in 'C:/Users/Rajnish/Desktop/GeeksforGeeks'  
print("Before saving image:")  

# Filename
filename = 'C:/Users/Dell/Desktop/Before Graduation project/workspace/images/test.jpg'

# Using cv2.imwrite() method
# Saving the image
cv2.imwrite(filename, img)

# List files and directories  
# in 'C:/Users / Rajnish / Desktop / GeeksforGeeks'  
print("After saving image:")  
print('Successfully saved')