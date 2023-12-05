import cv2
import matplotlib.pyplot as plt
import os, shutil
from PIL import Image

inpath1 = "./image/"
inpath2 = "./image/prep/"
outpath = "./image-parse/"

def Reformat_Image_With_Ratio(ImageFilePath, desired_aspect_ratio, name):
    
    image = Image.open(ImageFilePath, 'r')
    width = image.width
    height = image.height
    img_aspect_ratio = width/height
    
    if (img_aspect_ratio != desired_aspect_ratio):
        bigside = width if width > height else height
        other_side = int(bigside * desired_aspect_ratio)
        background = Image.new('RGBA', (other_side, bigside), (255, 0, 0, 255))
        offset = (int(round(((bigside - width) / 2), 0)), int(round(((bigside - height) / 2),0)))

        background.paste(image, offset)
        background.save(inpath2 + name.replace(".jpg",".png"))

os.mkdir(inpath2)

for file1 in os.listdir(inpath1):
    if file1.endswith(".jpg"):
        Reformat_Image_With_Ratio(inpath1 + file1, 640/420, file1)
        for file2 in os.listdir(inpath2):
            img=cv2.imread(inpath2 + file2)
            image = cv2.resize(img, (640,420))
            os.remove(inpath2 + file2)
            cv2.imwrite(inpath2 + file2.replace(".png",".jpg"), image)

for file in os.listdir(inpath2):
    if file.endswith(".jpg"):
        os.system("python exp/inference/inference.py  --loadmodel ./data/checkpoints/inference.pth --img_path " + inpath2 + file + " --output_path ./image-parse/ --output_name " + file)
        for filea in os.listdir(outpath):
            os.rename(outpath + filea, (outpath + filea).replace(".jpg.png", ".png"))

for file in os.listdir(outpath):
    if file.endswith(".jpg_gray.png"):
        os.remove(outpath + file)

for file in os.listdir(outpath):
    if file.endswith(".png"):
        img = cv2.imread(outpath + file)
        cropped = img[0:419, 53:366]
        cv2.imwrite(outpath + file, cropped)

for file in os.listdir(outpath):
    if file.endswith(".png"):
        img = cv2.imread(outpath + file)
        img = cv2.resize(img,(768,1024))
        cv2.imwrite(outpath + file, img)

shutil.rmtree(inpath2)

