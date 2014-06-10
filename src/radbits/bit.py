'''
Created on Jun 10, 2014

@author: lmosiman
'''
from math import sqrt, degrees, asin
from fractions import Fraction

class Bit(object):
    '''
    classdocs
    '''
    radius = []
    sin_of_angle = []
    angle = []
    rational_num = []


    def __init__(self):
        '''
        Constructor
        '''
    
    def get_bit_radius(self,cut_radius,cut_depth,sin_of_angle):
        self.radius = cut_radius*((2+(cut_depth/cut_radius)*((1/sin_of_angle**2)-1))/(2/sin_of_angle))
        self.radius = int(self.radius*16+1)/float(16)
        while self.radius >= cut_radius:
            self.radius -= .0625
        self.rep_as_fraction()
        
    def get_sin_of_bit_angle(self,cut_radius,cut_depth):
        try:
            self.sin_of_angle = (cut_depth/self.radius)/(1-sqrt(1-2*(cut_radius*cut_depth/(self.radius**2))+(cut_depth/self.radius)**2))
        except ValueError:
            self.sin_of_angle = self.radius/cut_radius
        except ZeroDivisionError:
            self.sin_of_angle = self.radius/cut_radius
        while self.sin_of_angle >= .707:
            self.radius -= .0625
            self.get_sin_of_bit_angle(cut_radius, cut_depth)
        self.get_angle()
        
    def get_angle(self):
        self.angle = round(degrees(asin(self.sin_of_angle)))
        
    def rep_as_fraction(self):
        frac = Fraction.from_float(self.radius)
        whole = int(frac.numerator)/int(frac.denominator)
        remainder = int(frac.numerator)%int(frac.denominator)
        self.rational_num = str(whole) + " " + str(remainder) + "/" + str(frac.denominator)
        
        