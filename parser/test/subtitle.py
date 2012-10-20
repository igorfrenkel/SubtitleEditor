'''
Created on Oct 19, 2012

@author: igor
'''
import unittest
from lib.subtitle import SubtitleDelta
from datetime import timedelta

class SubtitleProperties(unittest.TestCase):

    def test_subtitle_has_start_and_end(self):
        sub = SubtitleDelta('start', 'end')
        try:
            sub.start
        except AttributeError:
            self.fail("SubtitleDelta doesn't have a start")
        
        try:
            sub.end
        except AttributeError:
            self.fail("SubtitleDelta doesn't have an end")
            
    def test_two_subtitles_with_same_start_and_end_times_are_equal(self):
        self.assertEqual(SubtitleDelta(timedelta(), timedelta()), 
                         SubtitleDelta(timedelta(), timedelta()))
        
        
class SubtitleManipulatesTimedeltas(unittest.TestCase):
    
    def setUp(self):
        self.delta = timedelta(hours=155, minutes=10, seconds=15, milliseconds=130)
    
    def test_get_hours(self):
        self.assertEquals(155,
                          SubtitleDelta.hours(self.delta))
        
    def test_get_minutes(self):
        self.assertEquals(10,
                          SubtitleDelta.minutes(self.delta))
        
    def test_get_seconds(self):
        self.assertEquals(15,
                          SubtitleDelta.seconds(self.delta))
    
    def test_get_milliseconds(self):
        self.assertEquals(130,
                          SubtitleDelta.milliseconds(self.delta))
               

class SubtitleCanManipulateItsInterval(unittest.TestCase):
    
    def test_subtitle_can_add_time(self):
        sub = SubtitleDelta(timedelta(minutes=1), timedelta(minutes=2))
        sub.uptick_by(timedelta(minutes=120))
        self.assertEquals(timedelta(minutes=1, hours=2), sub.start)
        self.assertEquals(timedelta(minutes=2, hours=2), sub.end)
     
    def test_subtitle_can_remove_time(self):
        sub = SubtitleDelta(timedelta(minutes=1), timedelta(minutes=2))
        sub.downtick_by(timedelta(seconds=5))
        self.assertEquals(timedelta(minutes=0, seconds=55), sub.start)
        self.assertEquals(timedelta(minutes=1, seconds=55), sub.end)

class SubtitleHasAStringRepresentation(unittest.TestCase):

    def test_subtitle_is_a_reprsentation_of_its_start_and_end_time(self):
        self.assertEquals('00:01:11,000 --> 00:02:12,000', 
                          str(SubtitleDelta(timedelta(minutes=1, seconds=11), timedelta(minutes=2, seconds=12))))
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
