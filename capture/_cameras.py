from pypylon import pylon
import numpy as np
import cv2

class Camera:
    
    def __init__(self,cam_type):
                  
         if cam_type == 'Basler':
             self.cam_type = cam_type
             self.camera = Camera.loadBasler()
             
         elif cam_type == 'Webcam':
             self.cam_type = cam_type
             self.camera = Camera.loadWebCam()
             
         else:
             raise ValueError('Invalid camera type')
             
             
    
    def loadBasler():
        
        camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())
        camera.Open()
        
        print("Using device ", camera.GetDeviceInfo().GetModelName())
        
        return camera
    
    def loadWebCam():
        camera = cv2.VideoCapture(0)
        
        print("Device connected:", cv2.VideoCapture().isOpened())
               
        return camera
    
    def switch_type(self,cam_type):
        
        if self.cam_type == 'Basler':
            self.camera.Close()
            
            self.cam_type = cam_type
            self.camera = Camera.loadWebCam()
            
        elif self.cam_type == 'Webcam':
            self.camera.release()
            
            self.cam_type = cam_type
            self.camera = Camera.loadBasler()
        
        
        else:
            raise ValueError('invalid type selected')
    
    def snap(self, no_image=1):
        
        if self.cam_type == 'Basler':
            cam = self.camera
            
            cam.StartGrabbingMax(no_image)

   
            while cam.IsGrabbing():
                grabResult = cam.RetrieveResult(500, pylon.TimeoutHandling_ThrowException)
                
                if grabResult.GrabSucceeded():
                    img = grabResult.Array
                                       
                else:
                    print("Error: ", grabResult.ErrorCode, grabResult.ErrorDescription)
                    grabResult.Release()
            
            return img
            
        elif self.cam_type == 'Webcam':
            
            cam = self.camera
            ret, img = cam.read()           
            
            return img
            
        else:
            raise ValueError('No valid camera loaded')