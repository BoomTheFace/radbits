'''
Created on Jun 10, 2014

@author: lmosiman
'''

if __name__ == '__main__':
    pass

import bit
import cut

print "Welcome to RadBits v0.3 alpha!"
print "============================="

new_cut = cut.Cut()
new_bit = bit.Bit()

new_bit.get_bit_radius(new_cut.radius, new_cut.depth, new_cut.sin_of_min_angle)
new_bit.get_sin_of_bit_angle(new_cut.radius, new_cut.depth)

print "Bit radius: " ,new_bit.rational_num
print "Bit angle: " ,new_bit.angle