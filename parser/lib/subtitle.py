'''
Created on Oct 19, 2012

@author: igor
'''

class SubtitleDelta(object):
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
        return '%02d:%02d:%02d,%03d --> %02d:%02d:%02d,%03d' % (SubtitleDelta.hours(self.start),
                                          SubtitleDelta.minutes(self.start),
                                          SubtitleDelta.seconds(self.start),
                                          SubtitleDelta.milliseconds(self.start),
                                          SubtitleDelta.hours(self.end),
                                          SubtitleDelta.minutes(self.end),
                                          SubtitleDelta.seconds(self.end),
                                          SubtitleDelta.milliseconds(self.end))
    
    def __eq__(self, other):
        return self.start.total_seconds() == other.start.total_seconds() and self.end.total_seconds() == other.end.total_seconds()
    
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
        mills = round(delta.total_seconds() - cls.hours(delta)*3600 - cls.minutes(delta)*60 - cls.seconds(delta), 3)
        return int(mills*1000)
