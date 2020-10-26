import pixelator
import image_slicer
from image_slicer import join
import os, sys
from PIL import Image as imcon
from PIL import ImageDraw,ImageEnhance
from matplotlib import image as img
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import numpy as np
from scipy.cluster.vq import whiten
from scipy.cluster.vq import kmeans
import cv2

startpath = "/Users/campberebe3/Desktop/averageface/FaceIn"
outpath = "/Users/campberebe3/Desktop/averageface/FaceOut"
gridoutpath = "/Users/campberebe3/Desktop/averageface/GridOut"

directory = os.listdir(startpath)
outputs = os.listdir(outpath)

pixelator.makeFolders(startpath,outpath,gridoutpath,directory,outputs)
newoutputs = pixelator.startCutting(startpath,outpath,gridoutpath,directory,outputs)
pixelator.makeNewColors(startpath,outpath,gridoutpath,directory,newoutputs)
pixelator.squareup(startpath,outpath,gridoutpath,directory,newoutputs)