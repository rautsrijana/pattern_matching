import cv2
import os
import numpy as np
from argparse import ArgumentParser


parser = ArgumentParser()

parser.add_argument('-i', '--image_folder', dest = 'image_folder')
parser.add_argument('-m', '--mask_folder', dest = 'mask_folder')
parser.add_argument('-o', '--output_folder', dest = 'output_folder')
args = parser.parse_args()


image_folder = args.image_folder
mask_folder = args.mask_folder
output_folder = args.output_folder

list_images = os.listdir(image_folder)
list_mask = os.listdir(mask_folder)

if not os.path.exists(output_folder):
    os.makedirs(output_folder, )

def crop_image_from_mask(image, mask):
    mask = cv2.cvtColor(mask, cv2.COLOR_RGB2GRAY)
    analysis = cv2.connectedComponentsWithStats(mask, 4, cv2.CV_32S)
    (nub_labels, label_matrix, stats, centroids) = analysis
    largest_area = stats.max()
    list_bb = []
    for item in stats:
        if not largest_area in item:
            list_bb.append(item)
    list_bb = np.array(list_bb)
    if list_bb[0,0]>list_bb[1,0]:
        left_bbox = list_bb[1]
        right_bbox = list_bb[0]
    else:
        left_bbox = list_bb[0]
        right_bbox = list_bb[1]
    x_right = right_bbox[0]+right_bbox[2]
    y_right = right_bbox[1]+right_bbox[3]

    x_left = left_bbox[0] #correct
    y_left = min(left_bbox[1], right_bbox[1]) #correct
    w = x_right-x_left #correct
    h = max(y_right, left_bbox[1]+left_bbox[3])-min(y_left, right_bbox[1])
    new_bbox = [x_left, y_left, w, h]
    
    X,Y,W,H = new_bbox
    cropped_image = image[Y:Y+H, X:X+W]
    return cropped_image


for img_path, mask_path in zip(list_images,list_mask):
    image = cv2.imread(os.path.join(image_folder,img_path))
    mask = cv2.imread(os.path.join(mask_folder, mask_path))
    print(image)
    print(mask)
    cropped_image = crop_image_from_mask(image, mask)
    cv2.imwrite( os.path.join(output_folder, os.path.basename(mask_path)), cropped_image)



