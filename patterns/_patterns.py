# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 14:22:05 2022

@author: ezzln1
"""

import numpy as np

class Fringe:
    
    def __init__(self,size,period,phase_step,dimension ='horizontal',**method):
        
        self.period = period
        self.phase_step = phase_step
        self.dimension = dimension
        self.method = method['method']
        
        if self.method == 'three-phase':
            patterns = pattern_gen(size, 
                                   period, 
                                   phase_step,
                                   dimension,
                                   method=self.method)
            
        elif self.method == 'carre':
            patterns = pattern_gen(size, 
                                   period, 
                                   phase_step,
                                   dimension,
                                   method=self.method)
            
        elif self.method == 'hariharan':
            patterns = pattern_gen(size, 
                                   period, 
                                   phase_step,
                                   dimension,
                                   method=self.method)
            
        elif self.method == 'N-least-squares':
            patterns = pattern_gen(size, 
                                   period, 
                                   phase_step,
                                   dimension,
                                   method=self.method,
                                   images=method['no_images'])
            
        else:
            raise ValueError('invalid method: try three-phase, carre, hariharan or N-least-squares')
                
        self.patterns = patterns
        

def pattern_gen(size, period, phase_step, dimension ='horizontal',**method):
    
    w = size[1]
    h = size[0]
        
    x,y = np.meshgrid(range(w),range(h))
    
    if method['method'] == 'three-phase':
        k  = [-1, 0, 1]
            
    elif method['method'] == 'carre':
        k = [-3, -1, 1, 3]
            
    elif method['method'] == 'hariharan':
        k = [-2,-1, 0, 1, 2]
            
    elif method['method'] == 'N-least-squares':
        k = range(0,method['no_images'])
            
    else:
        raise ValueError('invalid method: try three-phase, carre, hariharan or N-least-squares')
        
    patterns = []
    
    for i in range(len(k)):
        
        if dimension == 'horizontal':
            img = 255/2*(1 + np.cos(2*np.pi*x/period + float(k[i])*phase_step))
            patterns.append(img)
                
        elif dimension == 'vertical':
            img = 255/2*(1 + np.cos(2*np.pi*y/period + float(k[i])*phase_step))
            patterns.append(img)
                
        else:
            raise ValueError('horizontal or vertical images?')
        
    return patterns
  
       
def gamma_correction(fringe):
    
    for i, img in enumerate(fringe.patterns):
        pass

    
        