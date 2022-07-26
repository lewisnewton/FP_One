# -*- coding: utf-8 -*-

import numpy as np
import screeninfo as si
import cv2

def screens():
    
    screen_ids = si.get_monitors()
          
    return screen_ids


class Projector():
    
    def __init__(self,screen_id):
        self.screen_id = screen_id
        self.screen = si.get_monitors()[self.screen_id]       
        self.width = self.screen.width
        self.height = self.screen.height
        self.x = self.screen.x
        self.y = self.screen.y
        
    def change_screen(self,new_screen_id):
        self.screen_id = new_screen_id
        self.screen = si.get_monitors()[self.screen_id]
        self.width = self.screen.width
        self.height = self.screen.height
        self.x = self.screen.x
        self.y = self.screen.y
    
    def size(self):
        dimension = [self.width, self.height]
        return dimension
        
    def project_test(self):
        img =  np.ones([self.width,self.height])
        
        window_name = "project_test"
        
        cv2.namedWindow(window_name,cv2.WND_PROP_FULLSCREEN)
        cv2.moveWindow(window_name, self.x - 1,self.y - 1)
        cv2.setWindowProperty(window_name,cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
        cv2.imshow(window_name ,img)
        cv2.waitKey()
        cv2.destroyAllWindows()
    
    def project(self, image, image_name):
        
        if image_name:
            window_name = "image"
        else:
            window_name = image_name
        
        cv2.namedWindow(window_name,cv2.WND_PROP_FULLSCREEN)
        cv2.moveWindow(window_name, self.x - 1,self.y - 1)
        cv2.setWindowProperty(window_name,cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
        cv2.imshow(window_name ,image)
        cv2.waitKey()
        cv2.destroyAllWindows()
    