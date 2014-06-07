'''
RadBits

June 6, 2014

Lucas Mosiman
'''

class Cut():
    def __init__(self,depth,radius,error):
        self.depth = depth
        self.radius = radius
        self.error = error
    def get_sin_of_angle(self,depth,radius,error):
        '''
        