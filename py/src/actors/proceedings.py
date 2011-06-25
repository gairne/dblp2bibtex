"""
This file is part of the dblp2xml project

This project is licensed under the Creative Commons
Attribution-NonCommercial-ShareAlike 3.0 Unported License.

See LICENSE under the project's top level directory.

Copyright (c) 2011 Matthew Mole <code@gairne.co.uk>
"""


# From http://en.wikipedia.org/wiki/Bibtex
# proceedings
#
#    The proceedings of a conference.
#    Required fields: title, year
#    Optional fields: editor, publisher, organization, address, month, note, key

class Proceedings:

    def __init__(self):
        self.records = {}

    def setElementValue(self, elementName, elementValue):
        try:
            if (type(self.records[elementName]) == type([])):
                self.records[elementName] += [elementValue]
            else:
                self.records[elementName] = [self.records[elementName]]
                self.records[elementName] += [elementValue]
        except:
            self.records[elementName] = elementValue

    def toBibtex(self):
        return str(self.records)

    """
    Checks to see that the required fields are all filled in.

    TODO: Title is a non-zero length string
    TODO: Year is a valid number between 1900 and something sensible
    """
    def isValid(self):
        try:
            return self.records["title"] != "" and \
                self.records["year"] != ""
        except:
            return False

if __name__ == '__main__':
    i = Proceedings()
    i.setElementValue("year", "2011")
    i.setElementValue("title", "")
    print "%s" % i.toBibtex()
    print "Is Valid: %s" % i.isValid()

    i = Proceedings()
    i.setElementValue("year", "20d1")
    i.setElementValue("title", "My Paper")
    print "%s" % i.toBibtex()
    print "Is Valid: %s" % i.isValid()

    i = Proceedings()
    i.setElementValue("year", "2011")
    i.setElementValue("title", "My Paper")
    print "%s" % i.toBibtex()
    print "Is Valid: %s" % i.isValid()