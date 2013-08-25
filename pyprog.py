import pygame, sys
from pygame.locals import *
import pygame.camera
pygame.init()
pygame.camera.init()
cam = pygame.camera.Camera("/dev/video1",(320,240))
cam.start()
image = cam.get_image()
pygame.image.save(image,'/home/pi/gitDownloads/camera/snap.ICB')
cam.stop()
