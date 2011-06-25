"""
This file is part of the dblp2xml project

This project is licensed under the Creative Commons
Attribution-NonCommercial-ShareAlike 3.0 Unported License.

See LICENSE under the project's top level directory.

Copyright (c) 2011 Matthew Mole <code@gairne.co.uk>
"""

import xml.sax

class XMLParser(xml.sax.ContentHandler):
    def startElement(self, elementName, attributes):
        if elementName == "inproceedings":
            for (k,v) in attributes.items():
                print k + " " + v
        elif elementName == "proceedings":
            for (k,v) in attributes.items():
                print k + " " + v

    def endElement(self, elementName):
        pass

    def characters(self, content):
        pass

parser = xml.sax.make_parser()
parser.setContentHandler(XMLParser())
parser.parse(open("../../../dblp.xml","r"))

if __name__ == '__main__':
    parser.setContentHandler(XMLParser())
    parser = xml.sax.make_parser()
    parser.parse(open("../../../dblp.xml","r"))
