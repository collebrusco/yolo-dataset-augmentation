import os

def list_filenames(directory_path, output_file_name):
    file_names = os.listdir(directory_path)

    with open(output_file_name, 'w') as output_file:
        for file_name in file_names:
            output_file.write('./' + directory_path + '/' + file_name + '\n')


if __name__ == '__main__':
	list_filenames('images/Train', 'train.txt')
	list_filenames('images/Test', 'test.txt')
	list_filenames('images/Validation', 'val.txt')
