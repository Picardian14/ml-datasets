from PIL import Image
import os

sourceFolder = './train/pneumonia/'
for filename in os.listdir(sourceFolder):
    im = Image.open(sourceFolder+filename)
    imFlip = im.transpose(Image.FLIP_LEFT_RIGHT)
    crop = im.crop((100,100,500,500))
    im.thumbnail((400,400))
    im.save(sourceFolder + filename)
sourceFolder = './train/normal/'    
for filename in os.listdir(sourceFolder):
    im = Image.open(sourceFolder+filename)
    imFlip = im.transpose(Image.FLIP_LEFT_RIGHT)
    crop = im.crop((100,100,500,500))
    im.thumbnail((400,400))
    im.save(sourceFolder + filename)
sourceFolder = './val/pneumonia/'        
for filename in os.listdir(sourceFolder):
    im = Image.open(sourceFolder+filename)
    imFlip = im.transpose(Image.FLIP_LEFT_RIGHT)
    crop = im.crop((100,100,500,500))
    im.thumbnail((400,400))
    im.save(sourceFolder + filename)
sourceFolder = './val/normal/'        
for filename in os.listdir(sourceFolder):
    im = Image.open(sourceFolder+filename)
    imFlip = im.transpose(Image.FLIP_LEFT_RIGHT)
    crop = im.crop((100,100,500,500))
    im.thumbnail((400,400))
    im.save(sourceFolder + filename)



