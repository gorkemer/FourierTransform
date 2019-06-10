import numpy as np
 import scipy
 import scipy.misc
 import matplotlib.pyplot as plt
 from scipy import ndimage
 from PIL import Image

 img = Image.open('gorkem.png').convert('L')
 img.save('output_file.jpg')

 f = np.fft.fft2(img)
 fshift = np.fft.fftshift(f) ## shift for centering 0.0 (x,y)
 magnitude_spectrum = 20*np.log(np.abs(fshift))

 plt.subplot(121),plt.imshow(img, cmap = 'gray')
 plt.title('Input Image'), plt.xticks([]), plt.yticks([])
 plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
 plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
 plt.show()

 ## removing low frequency contents by applying a 60x60 rectangle window (for masking)
 rows = np.size(img, 0) #taking the size of the image
 cols = np.size(img, 1)
 crow, ccol = rows/2, cols/2

 fshift[crow-30:crow+30, ccol-30:ccol+30] = 0
 f_ishift= np.fft.ifftshift(fshift)

 img_back = np.fft.ifft2(f_ishift) ## shift for centering 0.0 (x,y)
 img_back = np.abs(img_back)

 plt.subplot(131),plt.imshow(img, cmap = 'gray')
 plt.title('Input Image'), plt.xticks([]), plt.yticks([])
 plt.subplot(132),plt.imshow(img_back, cmap = 'gray')
 plt.title('Image after removing low freq'), plt.xticks([]), plt.yticks([])
