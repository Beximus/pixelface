import image_slicer
from image_slicer import join
import os, sys
from matplotlib import image as img
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import numpy as np
from scipy.cluster.vq import whiten
from scipy.cluster.vq import kmeans
from PIL import Image

# NEED TO SPLIT IMAGES INTO RESPECTIVE FOLDERS
# NEED TO PROCESS EACH IMAGE IN FOLDER
# NEED TO REJOIN EACH IMAGE INTO SINGLE PIXELART IMAGE

startpath = "/Users/campberebe3/Desktop/averageface/CuttingFaces"
outpath = "/Users/campberebe3/Desktop/averageface/CutFaces"

directory = os.listdir(startpath)
outputs = os.listdir(outpath)


def startCutting():
    for picture in directory:
        newFolderName = os.path.splitext(picture)[0]
        folderpath = outpath+"/"+newFolderName
        os.mkdir(folderpath)
        inputpath = startpath+"/"+picture
        outputpath = folderpath
        print(inputpath)
        print(outpath)
        tiles = image_slicer.slice(inputpath,256,save=False)
        image_slicer.save_tiles(tiles,directory=outputpath,prefix='slice',format='png')
    print("words")
    

def makeFolders():
    for picture in directory:
        newFolderName = os.path.splitext(picture)[0]
        folderpath = outpath+"/"+newFolderName
        os.mkdir(folderpath)
        # inputpath = startpath+"/"+picture
        # outputpath = folderpath
        # print(inputpath)
        # print(outpath)
        # tiles = image_slicer.slice(inputpath,256,save=False)
        # image_slicer.save_tiles(tiles,directory=outputpath,prefix='slice',format='png')
    print("words")

def joinUp():
    root = outputs
    for folder in root:
        if not folder.startswith('.'):
            newpath = outpath+"/"+str(folder)
            print(newpath)
            nextFolder = os.listdir(newpath)
            for tile in nextFolder:
                currentpicture = tile
                print(currentpicture)
                tile.image = Image.open(currentpicture)

def sliceup():
    for picture in directory:
        newFolderName = os.path.splitext(picture)[0]
        folderpath = outpath+"/"+newFolderName
        inputpath = startpath+"/"+picture
        outputpath = folderpath
        tiles = image_slicer.slice(inputpath,256,save=False)
        image_slicer.save_tiles(tiles,directory=outputpath,prefix='slice',format='png')

sliceup()

        



