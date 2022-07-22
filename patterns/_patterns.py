# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 14:22:05 2022

@author: ezzln1
"""

import numpy as np

class Fringe:
    
    def __init__(self,size,n_image,period,phase,dimension ='horizontal'):
        
        self.period = period
        self.phase = phase
        self.dimension = dimension
        
        w = size[1]
        h = size[0]
        
        x,y = np.meshgrid(range(w),range(h))
        
        patterns = []
        
        for i in range(n_image):
            
            if self.dimension == 'horizontal':
                img = np.sin(2*np.pi/self.period*x)
                patterns.append(img)
                
            elif self.dimesion == 'vertical':
                img = np.np.sin(2*np.pi / self.period)*y
                patterns.append(img)
                
            else:
                raise ValueError('horizontal or vertical images?')
                
        self.patterns = patterns
       
    def gamma_correction(self, gamma):
    
        for i, img in enumerate()
        pass
        