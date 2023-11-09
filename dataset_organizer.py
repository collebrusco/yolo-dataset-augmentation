import os
import pandas as pd
import shutil
import glob


def create_train_test_splt():

    # Assuming DL is your DataFrame and it has columns 'filename' and 'Train_Val_Test'
    DL = pd.read_csv('DL_info.csv', nrows=693)  # replace 'your_dataframe.csv' with your actual csv file

    # Get the unique values in 'Train_Val_Test' column
    categories = str(DL['Train_Val_Test'].unique())

    # Create directories for each category if not exist
    for category in categories:
        os.makedirs(category, exist_ok=True)

    # Move the files to corresponding directories
    for index, row in DL.iterrows():
        # Extract the slice number from the filename
        s = row['File_name']
        base, ext = os.path.splitext(s)
        base = 'Images_nifti/' + base.rsplit('_', 1)[0]
        pattern = base + '_*-*.nii.gz'
        matching_files = glob.glob(pattern)


        if matching_files:
            print(f"Found file: {matching_files[0]}")
        else:
            print("No matching file found.")
            print(pattern, base)
            continue
        
        # Assume the first match is the correct file
        nifti_file = matching_files[0]
        
        category = str(row['Train_Val_Test'])
        destination = os.path.join(category, os.path.basename(nifti_file))
        shutil.move(nifti_file, destination)

def create_lesion_subfolders(path):
        # Assuming DL is your DataFrame and it has columns 'filename' and 'Train_Val_Test'
    DL = pd.read_csv('DL_info.csv', nrows=693)  # replace 'your_dataframe.csv' with your actual csv file

    # Get the unique values in 'Train_Val_Test' column
    categories = str(DL['Train_Val_Test'].unique())

    # Create directories for each category if not exist
    for category in categories:
        os.makedirs(category, exist_ok=True)

    # Move the files to corresponding directories
    for index, row in DL.iterrows():
        # Extract the slice number from the filename
        s = row['File_name']
        base, ext = os.path.splitext(s)
        base = 'Images_nifti/' + base.rsplit('_', 1)[0]
        pattern = base + '_*-*.nii.gz'
        matching_files = glob.glob(pattern)


        if matching_files:
            print(f"Found file: {matching_files[0]}")
        else:
            print("No matching file found.")
            print(pattern, base)
            continue
        
        # Assume the first match is the correct file
        nifti_file = matching_files[0]
        
        category = str(row['Train_Val_Test'])
        destination = os.path.join(category, os.path.basename(nifti_file))
        shutil.move(nifti_file, destination)


if __name__ == '__main__':
    pass
