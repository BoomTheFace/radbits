'''
RadBits

June 6, 2014

Lucas Mosiman
'''

from math import sqrt
from math import asin
from math import degrees

cut_radius = float(input ("Enter cut radius: "))
cut_depth = float(input ("Enter cut depth: "))

def MinimumSinOfAngle(cut_depth,cut_radius,ERROR=0.01):
    minimum_sin_of_angle = 1/(sqrt(1+8*(ERROR/cut_radius)*(cut_radius**2/cut_depth**2)))
    return minimum_sin_of_angle

def GetBitRadius(cut_radius,cut_depth,minimum_sin_of_angle):
    bit_radius = cut_radius*((2+(cut_depth/cut_radius)*((1/minimum_sin_of_angle**2)-1))/(2/minimum_sin_of_angle))
    bit_radius = int(bit_radius * 8+1)/float(8)
    while bit_radius >= cut_radius:
        bit_radius -= .125    
    return bit_radius

def GetBitAngle(cut_depth,cut_radius,bit_radius):
    try:
        try:
            bit_angle = (cut_depth/bit_radius)/(1-sqrt(1-2*(cut_radius*cut_depth/bit_radius**2)+(cut_depth/bit_radius)**2))
            bit_angle = GetAngleInDegrees(bit_angle)
        except ZeroDivisionError:
            print cut_depth, cut_radius, bit_radius
            bit_angle = bit_radius/cut_radius
            bit_angle = round(degrees(asin(bit_angle)))          
        return bit_angle
            
    except ValueError:
        bit_angle = bit_radius/cut_radius
        bit_angle = round(degrees(asin(bit_angle)))
    return bit_angle

def GetAngleInDegrees(sin_of_angle):
    angle_in_degrees = round(degrees(asin(sin_of_angle)))
    return angle_in_degrees


minimum_sin_of_angle = MinimumSinOfAngle(cut_depth,cut_radius)
bit_radius = GetBitRadius(cut_radius,cut_depth,minimum_sin_of_angle)
angle_in_degrees = GetAngleInDegrees(minimum_sin_of_angle)
bit_angle = GetBitAngle(cut_depth, cut_radius, bit_radius)

while bit_angle > 45:
    bit_radius -= .125
    bit_angle = GetBitAngle(cut_depth,cut_radius,bit_radius)

print "Bit angle: ",bit_angle
print "Bit radius: ",bit_radius

input("Press <enter> to quit.")