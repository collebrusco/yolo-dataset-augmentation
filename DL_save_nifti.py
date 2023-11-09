"""
Rewritten, should upscale the PNG file and then store it in the correct subfloder for
Train, Test, Validation split
"""

import numpy as np
import os
import cv2
import csv
import matplotlib.pyplot as plt


dir_in = 'Images_png'
dir_out = 'Dataset'
info_fn = 'DL_info.csv'  # file name of the information file


def load_slice(path):
    """load slices from 16-bit png files"""
    im = cv2.imread(path, -1)  # -1 is needed for 16-bit image
    assert im is not None, 'error reading %s' % path

    # the 16-bit png file has a intensity bias of 32768
    return (im.astype(np.int32) - 32768).astype(np.int16)


def read_DL_info():
    """read spacings and image indices in DeepLesion"""
    name = []
    train_test_split = []
    with open(info_fn, 'r') as csvfile:
        reader = csv.reader(csvfile)
        rownum = 0
        for row in reader:
            if rownum == 0:
                header = row
                rownum += 1
            else:
                temp_name = row[0]
                 # Split the filename into parts
                parts = temp_name.split('_')

                # Reassemble the parts into the new format
                new_filename = f"{dir_in}/{'_'.join(parts[:3])}/{parts[3]}"

                name.append(new_filename)

                train_test_split.append(row[17])

    name = np.array(name)
    train_test_split = np.array(train_test_split)
    return name, train_test_split


if __name__ == '__main__':
    images, split = read_DL_info()
    if not os.path.exists(dir_out):
        os.mkdir(dir_out)

    # Create Paths
    train_path = os.path.join(dir_out,'Train')
    test_path = os.path.join(dir_out, 'Test')
    validate_path = os.path.join(dir_out, 'Validation')

    for idx, image_path in enumerate(images):
        # Check is path is available
        if not os.path.exists(image_path):
            continue

        # Print Image Path
        print("Converting", image_path)
        
        # Convert the image
        load_image = load_slice(image_path)

        # Save in folder based on train_test_split
        if split[idx] == '1':
            # Generate png file name
            parts = image_path.split('/')

            # Extract the filename part and remove the extension
            new_filename = parts[-2] + '_' + parts[-1]

            # Part of training set
            final_path = os.path.join(train_path, new_filename)

            # Save converted file
            plt.imsave(final_path, load_image, cmap='gray')
        elif split[idx] == '2':
            # Generate png file name
            parts = image_path.split('/')

            # Extract the filename part and remove the extension
            new_filename = parts[-2] + '_' + parts[-1]

            # Part of training set
            final_path = os.path.join(validate_path, new_filename)

            # Save converted file
            plt.imsave(final_path, load_image, cmap='gray')
        elif split[idx] == '3':
            # Generate png file name
            parts = image_path.split('/')

            # Extract the filename part and remove the extension
            new_filename = parts[-2] + '_' + parts[-1]

            # Part of training set
            final_path = os.path.join(test_path, new_filename)

            # Save converted file
            plt.imsave(final_path, load_image, cmap='gray')
