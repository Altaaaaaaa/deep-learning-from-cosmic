import matplotlib.pyplot as plt
from matplotlib.image import imread

img = imread('mapple.jpg') # 이미지 읽어서 변수에 담아 둠.

plt.imshow(img)
plt.show()
