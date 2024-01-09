import os
import pygame




BASE_IMAGE_PATH = 'data/images/'

def load_image(path):
    img = pygame.image.load(BASE_IMAGE_PATH + path).convert()
    img.set_colorkey((0,0,0))
    return img

def load_images(path):
    images = []
    for img_name in os.listdir(BASE_IMAGE_PATH + path): #os.listdir is to list all the files in a directory
        images.append(load_image(path + '/' + img_name))
    return images