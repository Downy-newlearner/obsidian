# simple image processing

from skimage import io 
from tkinter.filedialog import askopenfilename  # choose file

import matplotlib.pyplot as plt
import matplotlib.image as mpimg 
import numpy as np  # numpy 추가

fname = askopenfilename()           # choose image file
image = mpimg.imread(fname)         # read image
plt.imshow(image)                   # display image 
plt.axis('off')  # 축 제거
plt.show()

# type of image object
print(type(image))

# image shape
print(image.shape)

# image data
print(image[:,:,1])  # red channel


# color to gray
from skimage import color 

gray_image = color.rgb2gray(image)
print(gray_image.shape)
plt.imshow(gray_image, cmap='gray')  
plt.axis('off')  # 축 제거
plt.show()

# resize
from skimage import transform 

new_shape = (image.shape[0] // 2, image.shape[1] // 2)  # 채널 수는 필요 없음
small = transform.resize(image=image, 
        output_shape=new_shape)

print(small.shape)
plt.imshow(small)
plt.axis('off')  # 축 제거
plt.show()
              

# flip, rotate
from skimage.transform import rotate

plt.imshow(np.fliplr(image))  # flip
plt.axis('off')  # 축 제거
plt.show()

plt.imshow(rotate(image, angle=45, resize=True))  # rotate (resize=True 추가)
plt.axis('off')  # 축 제거
plt.show()


# filters
from skimage.filters import sobel
plt.imshow(sobel(gray_image))  # sobel_h 대신 sobel 사용
plt.axis('off')  # 축 제거
plt.show()

# save image
io.imsave("d:/data/test2.png", image)
