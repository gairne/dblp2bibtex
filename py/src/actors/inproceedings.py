"""
This file is part of the dblp2xml project

This project is licensed under the Creative Commons
Attribution-NonCommercial-ShareAlike 3.0 Unported License.

See LICENSE under the project's top level directory.

Copyright (c) 2011 Matthew Mole <code@gairne.co.uk>
"""

From http://en.wikipedia.org/wiki/Bibtex
# inproceedings
#
#    An article in a conference proceedings.
#    Required fields: author, title, booktitle, year
#    Optional fields: editor, series, pages, organization, publisher, address, month, note, key

class Inproceedings:

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

    TODO: Author is a list with filled in elements
    TODO: Title and Booktitle is a non-zero length string
    TODO: Year is a valid number between 1900 and something sensible
    """
    def isValid(self):
        try:
            return self.records["author"] != "" and \
                self.records["title"] != "" and \
                self.records["booktitle"] != "" and \
                self.records["year"] != ""
        except:
            return False

if __name__ == '__main__':
    i = Inproceedings()
    i.setElementValue("author", "First Last")
    i.setElementValue("author", "John L\\\"ubeck")
    i.setElementValue("author", "Michael D. Lemon")
    print "%s" % i.toBibtex()
    print "Is Valid: %s" % i.isValid()

    i = Inproceedings()
    i.setElementValue("author", "")
    i.setElementValue("booktitle", "ISMM")
    i.setElementValue("year", "2011")
    i.setElementValue("title", "My Paper")
    print "%s" % i.toBibtex()
    print "Is Valid: %s" % i.isValid()

    i = Inproceedings()
    i.setElementValue("author", "First Last")
    i.setElementValue("booktitle", "ISMM")
    i.setElementValue("year", "20d1")
    i.setElementValue("title", "My Paper")
    print "%s" % i.toBibtex()
    print "Is Valid: %s" % i.isValid()

    i = Inproceedings()
    i.setElementValue("author", "First Last")
    i.setElementValue("booktitle", "ISMM")
    i.setElementValue("year", "2011")
    i.setElementValue("title", "My Paper")
    print "%s" % i.toBibtex()
    print "Is Valid: %s" % i.isValid()