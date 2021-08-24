import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET
import cv2
import math
from copy import deepcopy

objects_dict = {'Pedestrian':1,
                'Crosswalk':2,
                'Bike':3,
                'Car':4, 
                'Truck':5,
                'GreenLight':6,
                'GreenTrafficLight':7,
                'RedLight':8,
                'RedTrafficLight':9}
                
object_height = {'Car': 160, 'Pedestrian': 175, 'Bike': 105, 'Bus': 299, 'Truck': 410, 'GreenLight': 120, 'GreenTrafficLight': 120, 'RedLight': 120, 'RedTrafficLight': 120, 'Crosswalk': 20}
object_width = {'Car': 180, 'Pedestrian': 55, 'Bike': 42, 'Bus': 255, 'Truck': 260, 'GreenLight': 40, 'GreenTrafficLight': 40, 'RedLight': 40, 'RedTrafficLight': 40, 'Crosswalk': 375}
object_breadth = {'Car': 400, 'Pedestrian': 30, 'Bike': 175, 'Bus': 1195, 'Truck': 1400, 'GreenLight': 50, 'GreenTrafficLight': 50, 'RedLight': 50, 'RedTrafficLight': 50, 'Crosswalk': 937}

def xml_to_csv(path, file_name, class_name = None ):
    image_height = set()
    image_width = set()
    path = os.path.join(os.getcwd(), path)
    xml_list = []
    
    if class_name != None:
    	inference = True
    else:
    	inference = False
    	
    for xml_file in glob.glob(path + '/*.xml'):
        
        img_file = xml_file.replace('xml', 'jpg') # image_location
        img = cv2.imread(img_file)
        img_width = img.shape[1]
        img_height = img.shape[0]
        image_height.add(img_height)
        image_width.add(img_width)

        name_list = xml_file.split("/")
 
        if inference == True: # for inference
            distance = name_list[-1].split('_')[0]
        else:
            class_name = name_list[-1].split('_')[0] 
            distance = name_list[-1].split('_')[1]
            
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall('object'):
            value = (root.find('filename').text,
                     int(root.find('size')[0].text),
                     int(root.find('size')[1].text),
                     member[0].text,
                     int(member[4][0].text),
                     int(member[4][1].text),
                     int(member[4][2].text),
                     int(member[4][3].text),
                     int(member[4][3].text)-int(member[4][1].text),
                     int(member[4][2].text)-int(member[4][0].text),
                     objects_dict[member[0].text],
                     # 1/Bh
                     (1 / ((int(member[4][3].text)-int(member[4][1].text))/ img_height)),
                     # 1/Bw
                     (1 / ((int(member[4][2].text)-int(member[4][0].text))/ img_width)),
                     # 1/Bd - math.sqrt(FRAME_WIDTH ** 2 + FRAME_HEIGHT ** 2 )
                     (1 / ( math.sqrt( (int(member[4][2].text)-int(member[4][0].text))**2 + ( (int(member[4][3].text)-int(member[4][1].text)) **2) ) / ( math.sqrt(img_width ** 2 + img_height ** 2 )) )),
                     float(object_height[member[0].text]),
                     float(object_width[member[0].text]),
                     float(object_breadth[member[0].text]),
                     float(distance)
                     )
            xml_list.append(value)
    column_name = ['filename', 'image_width', 'image_height', 'object_name', 'xmin', 'ymin', 'xmax', 'ymax', 'bb_height', 'bb_width', 'object_class', '1/Bh', '1/Bw', '1/Bd', 'Ch', 'Cw', 'Cb', 'distance_ft']
    image_width = list(image_width)[0]
    image_height = list(image_height)[0]
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    xml_df.to_csv('./workspace/csv/'+file_name, index=False)
    return image_height, image_width

 
