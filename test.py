# -*- coding: utf-8 -*-
"""
Created on Wed May 08 14:53:52 2013

@author: kshmirko
"""

import lxml.html
import urllib

from parse.parse import parse_observation, ParserException
data=None
with open('meteo.html') as f:
    data = f.read()

#data = urllib.urlopen('http://weather.uwyo.edu/cgi-bin/sounding?region=naconf&TYPE=TEXT%3ALIST&YEAR=2013&MONTH=05&FROM=0712&TO=0900&STNM=31977').read()



doc = lxml.html.document_fromstring(data)

body = doc.xpath('/html/body')[0]

# select all tags under body
children = [ item for item in body.iterchildren() ]
children.reverse()

try:
    # Parse output while the input isn't empty
    while True:
        parse_observation(children)
except ParserException, e:
    print e