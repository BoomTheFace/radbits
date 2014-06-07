'''
RadBits

June 6, 2014

Lucas Mosiman
'''

from math import sqrt
from math import asin
from math import degrees

class Cut():
    def __init__(self,depth,radius,error,sin_of_angle=0.0):
        self.depth = depth
        self.radius = radius
        self.error = error
        self.sin_of_angle = self.get_sin_of_angle()
    
    def get_sin_of_angle(self):
        '''
        sin alpha = 1/sqrt(1+8*(E/R)*(R**2/D**2)
        '''
        sin_of_angle = 1/sqrt(1+8*(self.error/self.radius)*(self.error**2/self.depth**2))
        return sin_of_angle

class Bit():
    def __init__(self,radius,angle,sin_of_angle):
        self.radius = radius
        self.angle = angle
        self.sin_of_angle = sin_of_angle
    
    def get_bit_radius(self,cut_radius,cut_depth,sin_of_angle):
        '''
        r = R * ((2+(D/R)*((1/sin(alpha)**2)-1)/(2/sin(alpha))
        '''
        bit_radius = cut_radius * ((2+(cut_depth/cut_radius)*((1/sin_of_angle**2)-1))/(2/sin_of_angle))
        return bit_radius
    
    def get_bit_angle(self,cut_depth,bit_radius,cut_radius):
        '''
        sin(alpha) = (D/r)/(1-sqrt(1-2*(R*D/r**2)+(D/r)**2))
        '''
        sin_of_angle = (cut_depth/bit_radius)/(1-sqrt(1-2*(cut_radius*cut_depth/bit_radius**2)+(cut_depth/bit_radius)**2))
        angle = round(degrees(asin(sin_of_angle)))
        return angle
    
    def adjust_bit(self,radius):
        '''
        round bit radius down to nearest 1/8th of an inch
        '''
        if radius % 8 == 0:
            return radius
        else:
            radius = (int(radius * 8)+1)/8