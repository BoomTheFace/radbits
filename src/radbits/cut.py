'''
Created on Jun 10, 2014

@author: lmosiman
'''
from math import sqrt

DEFAULT_ERROR = 0.01

class Cut(object):
    '''
    classdocs
    '''
    radius = []
    depth = []
    sin_of_min_angle = []
    margin_of_error = []  
    
    def __init__(self):
        '''
        Constructor
        '''
        self.set_radius()
        self.set_depth()
        self.set_margin_of_error()
        self.get_sin_of_min_angle()
    
    def set_radius(self):
        try:
            self.radius = float(input("Enter desired radius of cut: "))
            if self.radius == 0:
                print "ERROR: Radius must be greater than 0 (zero)."
                self.set_radius()
        except SyntaxError:
            print "ERROR: No radius entered."
            self.set_radius()
    
    def set_depth(self):
        try:
            self.depth = float(input("Enter desired depth of cut: "))
            if self.depth == 0:
                print "ERROR: Depth must be greater than 0 (zero)."
                self.set_depth()
        except SyntaxError:
            print "Error: No depth entered."
            self.set_depth()
    
    def set_margin_of_error(self):
        try:
            self.margin_of_error = float(input("Select margin of error (must be greater than 0), or press enter for default (0.01)"))
            if self.margin_of_error <= 0:
                print "Error must be greater than zero."
                self.set_margin_of_error()
        except SyntaxError:
            self.margin_of_error = DEFAULT_ERROR
            print "No margin of error entered; using default"
            
    def get_sin_of_min_angle(self):
        self.sin_of_min_angle = 1 / sqrt(1 + 8 * (self.margin_of_error / self.radius) * (self.radius ** 2 / self.depth ** 2))
        
