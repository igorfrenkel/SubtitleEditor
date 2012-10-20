'''
Created on Oct 19, 2012

@author: igor
'''

from lib.subtitle import SubtitleDelta
from datetime import timedelta
from re import match


class StringParser:

    def __init__(self, string):
        self.lines = []
        self.input_string = string
    
    def parse(self):
        lines = self.input_string.split("\n")
        for line in lines:
            self.lines.append(LineParser.parse(line))
        
    def uptick(self, delta):
        lines = []
        for line in self.lines:
            if isinstance(line, SubtitleDelta):
                line.uptick_by(delta)
            lines.append(line)
        self.lines = lines
        
    def downtick(self, delta):
        lines = []
        for line in self.lines:
            if isinstance(line, SubtitleDelta):
                line.downtick_by(delta)
            lines.append(line)
        self.lines = lines
        
    def __str__(self):
        return "\n".join(map(lambda x: str(x), self.lines))
    
class LineParser(object):
    delta_regex = '(\d{2}):(\d{2}):(\d{2}),(\d{3})'
    
    @classmethod
    def parse(cls, line_string):
        line_regex = '%s\s*-->\s*%s' % (cls.delta_regex, cls.delta_regex)
        matches = match(line_regex, line_string)
        if matches == None:
            return line_string
        str = line_string.split(' --> ')
        return SubtitleDelta(cls.get_timedelta_from_string(str[0]),
                             cls.get_timedelta_from_string(str[1]))

    
    @classmethod
    def get_timedelta_from_string(cls, string):
        matches = match(cls.delta_regex, string)
        return timedelta(hours = int(matches.group(1)),
                         minutes = int(matches.group(2)),
                         seconds = int(matches.group(3)),
                         milliseconds = int(matches.group(4)))
