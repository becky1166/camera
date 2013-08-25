import pygame, sys
from pygame.locals import *
import pygame.camera
pygame.init()
pygame.camera.init()
cam = pygame.camera.Camera("/dev/video0",(1920,1080))
screen = pygame.display.set_mode((1920,1080))
cam.start()
image = cam.get_image()
pygame.image.save(image,'/home/pi/gitDownloads/camera/snap.ICB')
screen.blit(image,(0,0))
pygame.display.flip()
cam.stop()
nb = raw_input('keyboard')
