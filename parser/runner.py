'''
Created on Oct 20, 2012

@author: igor
'''
from lib.parser import StringParser
from datetime import timedelta

if __name__ == '__main__':
    f = open('/Users/igor/.Trash/Musa - The Warrior .sm.srt','r')
    string = f.read()
    f.close()
    
    p = StringParser(string)
    p.parse()
    #p.uptick(timedelta(seconds=5))
    f = open ('/tmp/meow.srt', 'w')
    f.write(str(p))
    f.close()