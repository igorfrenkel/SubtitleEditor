'''
Created on Oct 19, 2012

@author: igor
'''

from lib.subtitle import Subtitle
from datetime import timedelta
from re import match


class StringParser:

    def __init__(self, string):
        self.lines = string.split("\n")
    
class LineParser(object):
    delta_regex = '(\d{2}):(\d{2}):(\d{2}),(\d{3})'
    
    @classmethod
    def parse(cls, line_string):
        line_regex = '%s\s*-->\s*%s' % (cls.delta_regex, cls.delta_regex)
        matches = match(line_regex, line_string)
        if matches == None:
            return line_string
        return [timedelta(), timedelta()]
    
    @classmethod
    def get_timedelta_from_string(cls, string):
        matches = match(cls.delta_regex, string)
        return timedelta(hours = int(matches.group(1)),
                         minutes = int(matches.group(2)),
                         seconds = int(matches.group(3)),
                         milliseconds = int(matches.group(4)))
