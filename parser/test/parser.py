'''
Created on Oct 19, 2012

@author: igor
'''
import unittest
from datetime import timedelta
from lib.parser import StringParser, LineParser
from lib.subtitle import Subtitle

class LineParserTimeIntervalMatching(unittest.TestCase):
    
    def test_parser_returns_same_line_given_if_not_matched_time_interval(self):
        invalid_line = 'Fear not, l will take this to your family'
        self.assertEqual('Fear not, l will take this to your family', LineParser.parse(invalid_line))
        
    def test_parser_returns_same_line_when_time_interval_incorrectly_formatted(self):
        invalid_line = '00:01:13,464 --> 00:01:17'
        self.assertEqual('00:01:13,464 --> 00:01:17', LineParser.parse(invalid_line))
        
        invalid_line = '00:01:13 --> x:00:01:17,464'
        self.assertEqual(invalid_line, LineParser.parse(invalid_line))

    def test_parser_returns_two_time_deltas_when_given_correctly_formed_time_interval(self):
        parsedLine = LineParser.parse('00:01:13,464 --> 00:01:17,696')
        self.assertTrue(isinstance(parsedLine[0], timedelta))
        self.assertTrue(isinstance(parsedLine[1], timedelta))

class TestLineParserCreatesTimeDeltas(unittest.TestCase):
    
    def test_time_delta_from_string(self):
        self.assertEqual(timedelta(hours=0, minutes=1, seconds=13, milliseconds=464), 
                        LineParser.get_timedelta_from_string('00:01:13,464'))

class StringParserDecomposition(unittest.TestCase):
    
    def setUp(self):
        self.subtitle_string = """2
00:01:04,788 --> 00:01:10,192
Take a lock of his hair back to Korea.

3
00:01:13,464 --> 00:01:17,696
Fear not, l will take this to your family.

4
00:01:25,809 --> 00:01:27,333
AD 1 3 75-The first year of the King WOO,
Korean Dynasty."""
        self.parser = StringParser(self.subtitle_string)

    def test_parser_can_process_a_string_of_subtitle_lines(self):
        parser = StringParser(self.subtitle_string)
        self.assertEqual(12, len(self.parser.lines))
        
    def test_parser_treats_non_subtitle_delta_lines_like_strings(self):
        self.assertEqual('4', self.parser.lines[8])
    
    def test_parser_instantiates_subtitle_delta_when_encountering_delta_line(self):
        self.assertTrue(isinstance(self.parser.lines[9], Subtitle))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
