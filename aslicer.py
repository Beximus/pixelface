import image_slicer
from image_slicer import join
import os, sys
from PIL import Image as imcon
from matplotlib import image as img
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import numpy as np
from scipy.cluster.vq import whiten
from scipy.cluster.vq import kmeans
import cv2
# NEED TO REJOIN EACH IMAGE INTO SINGLE PIXELART IMAGE

startpath = "/Users/campberebe3/Desktop/averageface/CuttingFaces"
outpath = "/Users/campberebe3/Desktop/averageface/CutFaces"

directory = os.listdir(startpath)
outputs = os.listdir(outpath)

# SPLITS UP THE IMAGE INTO 16 X 16 GRID

def startCutting():
    for file in directory:
        if not file.startswith('.'):
            newFolderName = os.path.splitext(file)[0]
            folderpath = outpath+"/"+newFolderName
            inputpath = startpath+"/"+file
            outputpath = folderpath
            tiles = image_slicer.slice(inputpath,256,save=False)
            image_slicer.save_tiles(tiles,directory=outputpath,prefix='slice',format='png')
    
# MAKES AS MANY FOLDERS AS THERE ARE IMAGES IN THE CUTTING FACES FOLDER    

def makeFolders():
    for picture in directory:
        if not picture.startswith('.'):
            newFolderName = os.path.splitext(picture)[0]
            folderpath = outpath+"/"+newFolderName
            os.mkdir(folderpath)

# MAKES A LIST OF IMAGES IN A GIVEN FOLDER (FOLDERPATH)

def montageList(filePath):
    folderPath = filePath
    currentFolder = os.listdir(filePath)
    tileList = [];
    for iterator,item in enumerate(currentFolder):
        currentPicture = folderPath+"/"+item
        tileList.append(currentPicture)
    return tileList

# NOT WORKING CURRENTLY  - WILL REJOIN PIXELS INTO SINGLE IMAGE

def joinUp():
    root = outputs
    for folder in root:
        if not folder.startswith('.'):
            newpath = outpath+"/"+str(folder)
            listOfTiles = montageList(newpath)
            weewoo = outpath+"/"+str(folder)+"/*.png"
            woowee = "./CutFaces"+str(folder)+"/newfile.jpg"
            print(listOfTiles)
            # print(listOfTiles)
            # print("\n")
            # command = "montage @{} -geometry +0+0 ".format(weewoo,woowee)
            # os.system(command)
            # # command =['montage', '-geometry','+0+0',imageLocat,newFile]
            # command = "montage -geometry +0+0 {} {}".format(imageLocat,newFile)
            # print(newline)
            # print(imageLocat)
            # print(command)
            # # os.system(command)
            # print("Done\n")
            
# CONVERTS PNG TILES INTO JPGS FOR REUNIFICATION

def makejpgimage(picturepath,startpath,newname):
    #"/Users/campberebe3/Desktop/averageface/CutFaces/Face342/slice_01_01.png"
    im = imcon.open(picturepath)
    newim = imcon.new("RGB",im.size,(255,255,255))
    newim.paste(im)
    newpath = startpath +"/"+newname
    newim.save(newpath)
    os.remove(picturepath)

# UNFINISHED FINDS DOMINANT COLOR OF GIVEN QUADRANT

def findDominantColor(picture):
    image = img.imread(picture)
    r = []
    g = []
    b = []

    for line in image:
        for pixel in line:
            temp_r, temp_g, temp_b = pixel
            r.append(temp_r)
            g.append(temp_g)
            b.append(temp_b)
                
    df = pd.DataFrame({'red': r,'blue': b,'green': g})

    df['scaled_red'] = whiten(df['red'])
    df['scaled_blue'] = whiten(df['blue'])
    df['scaled_green'] = whiten(df['green'])

    df.sample(n = 10)

    cluster_centers, distortion= kmeans(df[['scaled_red', 'scaled_green', 'scaled_blue']], 1)
    print(cluster_centers)

    colors = []
    r_std, g_std, b_std = df[['red', 'green', 'blue']].std()

    print(r_std)
    print(g_std)
    print(b_std)
    for cluster_center in cluster_centers:
        scaled_r, scaled_g, scaled_b = cluster_center
        colors.append((scaled_r*r_std/255,scaled_g*g_std/255,scaled_b*b_std/255))
    # plt.imshow([colors])
    # plt.show()
    print(colors)
    sizer = imcon.open(picture)
    width,height = sizer.size
    

# COMBINE THINGS TO MAKE THE PIXELS

def makeNewColors():
    for file in outputs:
        if not file.startswith('.'):
            imagepathstart = outpath +"/"+str(file)
            imagepathlist = montageList(imagepathstart)
            print("\nThis folder contains:")
            for path in imagepathlist:
                newImageName = os.path.splitext(os.path.basename(path))
                newImageName = str(newImageName[0])+".jpg"
                print(newImageName)
                makejpgimage(path,imagepathstart,newImageName)
                


def dothing():
    # makeFolders()
    # startCutting()
    # joinUp()
    findDominantColor("/Users/campberebe3/Desktop/averageface/CutFaces/Face394/slice_01_14.jpg")
    # findDominantColor('faceest.jpg')
    # makejpgimage("/Users/campberebe3/Desktop/averageface/CutFaces/Face342/slice_01_01.png","slice_01_01.png")
    # makeNewColors()


dothing()


        



