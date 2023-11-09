import nibabel as nib
import numpy as np
import matplotlib.pyplot as plt

test_load = nib.load('Images_nifti/000001_02_01_008-023.nii.gz').get_fdata()
print(test_load.shape)

test = test_load[:,:,0]
plt.imshow(test, cmap='gray')  # use the 'gray' colormap
plt.show()