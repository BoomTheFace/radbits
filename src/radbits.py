'''
RadBits

June 6, 2014

Lucas Mosiman
'''

from math import sqrt
from math import asin
from math import degrees

class Cut():
    def __init__(self,depth,radius,error=0.01,sin_of_angle=0.0):
        self.depth = depth
        self.radius = radius
        self.error = error
        self.sin_of_angle = self.get_sin_of_angle()
    
    def get_sin_of_angle(self):
        '''
        sin alpha = 1/sqrt(1+8*(E/R)*(R**2/D**2)
        '''
        sin_of_angle = 1/sqrt(1+8*(self.error/self.radius)*(self.radius**2/self.depth**2))
        return sin_of_angle
    
    def get_bit_radius(self):
        '''
        r = R * ((2+(D/R)*((1/sin(alpha)**2)-1)/(2/sin(alpha))
        '''
        bit_radius = self.radius * ((2+(self.depth/self.radius)*((1/self.sin_of_angle**2)-1))/(2/self.sin_of_angle))
        return bit_radius

class Bit():
    def __init__(self,radius,angle,sin_of_angle):
        self.radius = radius
        self.angle = angle
        self.sin_of_angle = sin_of_angle
    
    def get_bit_angle(self,cut_depth,bit_radius,cut_radius):
        '''
        sin(alpha) = (D/r)/(1-sqrt(1-2*(R*D/r**2)+(D/r)**2))
        '''
        sin_of_angle = (cut_depth/bit_radius)/(1-sqrt(1-2*(cut_radius*cut_depth/bit_radius**2)+(cut_depth/bit_radius)**2))
        angle = round(degrees(asin(sin_of_angle)))
        return angle
    
    def adjust_bit(self):
        '''
        round bit radius down to nearest 1/8th of an inch
        '''
        if radius % 8 == 0:
            return radius
        else:
            radius = (int(radius * 8)+1)/8
            
def get_degrees(sin_of_angle):
    '''
    convert sin of angle into degrees and round to nearest degree
    '''
    angle_in_degrees = round(degrees(asin(sin_of_angle)))
    return angle_in_degrees
            
new_cut = Cut(1,6)
angle = get_degrees(new_cut.get_sin_of_angle())
bit_radius = new_cut.get_bit_radius()
print angle
print bit_radius

