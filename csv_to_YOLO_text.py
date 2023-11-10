import pandas as pd
import os
import numpy as np
scan_info = pd.read_csv('DL_info.csv')
os.makedirs("labels", exist_ok=True)
os.makedirs("labels/Validation", exist_ok=True)
os.makedirs("labels/Test", exist_ok=True)
os.makedirs("labels/Train", exist_ok=True)

for filename in os.listdir("Dataset/Test"):
    
    entry = scan_info.loc[scan_info['File_name'] == filename]
    text_filename = filename.rsplit(".", 1)[0]+".txt"
    text_file = open("labels/Test/"+text_filename, 'w')
    bounding_box_coordinates_old = entry["Bounding_boxes"].iloc[0]
    bounding_box_coordinates = [float(idx) for idx in bounding_box_coordinates_old.split(', ')]
    bounding_box_category = entry["Coarse_lesion_type"]
    bounding_boxes = list()
    for x_first, y_first, x_second, y_second in zip(*[iter(bounding_box_coordinates)]*4):

        bounding_box = [(x_first+x_second)/(512*2), (y_first+y_second)/(512*2), np.abs(x_first-x_second)/(512), np.abs(y_first-y_second)/(512)]
        bounding_boxes.append(bounding_box)
    text_to_put_in = ""
    for bounding_box in bounding_boxes:
        text_to_put_in+= str(0)+" "+str(bounding_box[0])+" "+str(bounding_box[1])+" "+str(bounding_box[2])+" "+str(bounding_box[3])+"\n"
    
    text_file.write(text_to_put_in)

for filename in os.listdir("Dataset/Train"):
    
    entry = scan_info.loc[scan_info['File_name'] == filename]
    text_filename = filename.rsplit(".", 1)[0]+".txt"
    text_file = open("labels/Train/"+text_filename, 'w')
    bounding_box_coordinates_old = entry["Bounding_boxes"].iloc[0]
    bounding_box_coordinates = [float(idx) for idx in bounding_box_coordinates_old.split(', ')]
    bounding_box_category = entry["Coarse_lesion_type"]
    bounding_boxes = list()
    for x_first, y_first, x_second, y_second in zip(*[iter(bounding_box_coordinates)]*4):

        bounding_box = [(x_first+x_second)/(512*2), (y_first+y_second)/(512*2), np.abs(x_first-x_second)/(512), np.abs(y_first-y_second)/(512)]
        bounding_boxes.append(bounding_box)
    text_to_put_in = ""
    for bounding_box in bounding_boxes:
        text_to_put_in+= str(0)+" "+str(bounding_box[0])+" "+str(bounding_box[1])+" "+str(bounding_box[2])+" "+str(bounding_box[3])+"\n"
    
    text_file.write(text_to_put_in)

for filename in os.listdir("Dataset/Validation"):
    
    entry = scan_info.loc[scan_info['File_name'] == filename]
    text_filename = filename.rsplit(".", 1)[0]+".txt"
    text_file = open("labels/Validation/"+text_filename, 'w')
    bounding_box_coordinates_old = entry["Bounding_boxes"].iloc[0]
    bounding_box_coordinates = [float(idx) for idx in bounding_box_coordinates_old.split(', ')]
    bounding_box_category = entry["Coarse_lesion_type"]
    bounding_boxes = list()
    for x_first, y_first, x_second, y_second in zip(*[iter(bounding_box_coordinates)]*4):

        bounding_box = [(x_first+x_second)/(512*2), (y_first+y_second)/(512*2), np.abs(x_first-x_second)/(512), np.abs(y_first-y_second)/(512)]
        bounding_boxes.append(bounding_box)
    text_to_put_in = ""
    for bounding_box in bounding_boxes:
        text_to_put_in+= str(0)+" "+str(bounding_box[0])+" "+str(bounding_box[1])+" "+str(bounding_box[2])+" "+str(bounding_box[3])+"\n"
    
    text_file.write(text_to_put_in)
    