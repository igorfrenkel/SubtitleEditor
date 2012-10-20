'''
Created on Oct 19, 2012

@author: igor
'''

class Subtitle(object):
    '''
    classdocs
    '''

    def __init__(self, start, end):
        '''
        Constructor
        '''
        self.start = start
        self.end = end
      
    def uptick_by(self, delta):  
        self.start += delta
        self.end += delta
    
    def downtick_by(self, delta):
        self.start -= delta
        self.end -= delta
    
    def __str__(self):
        return '%02d:%02d:%02d,%03d --> %02d:%02d:%02d,%03d' % (Subtitle.hours(self.start),
                                               Subtitle.minutes(self.start),
                                               Subtitle.seconds(self.start),
                                               Subtitle.milliseconds(self.start),
                                               Subtitle.hours(self.end),
                                               Subtitle.minutes(self.end),
                                               Subtitle.seconds(self.end),
                                               Subtitle.milliseconds(self.end))
    
    @classmethod
    def hours(cls, delta):
        return int(delta.total_seconds()/3600)
    
    @classmethod
    def minutes(cls, delta):
        return int((delta.total_seconds() - cls.hours(delta)*3600)/60)
    
    @classmethod
    def seconds(cls, delta):
        return int((delta.total_seconds() - cls.hours(delta)*3600 - cls.minutes(delta)*60))
    
    @classmethod
    def milliseconds(cls, delta):
        return int((delta.total_seconds() - cls.hours(delta)*3600 - cls.minutes(delta)*60 - cls.seconds(delta))*1000)
