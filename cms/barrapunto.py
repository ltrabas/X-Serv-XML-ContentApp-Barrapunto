from xml.sax.handler import ContentHandler
from xml.sax import make_parser
import sys
import urllib2

class myContentHandler(ContentHandler):

    def __init__ (self):
        self.inItem = False
        self.inContent = False
        self.theContent = ""
        self.line = ""
        self.enlace = ""

    def startElement (self, name, attrs):
        if name == 'item':
            self.inItem = True
        elif self.inItem:
            if name == 'title':
                self.inContent = True
            elif name == 'link':
                self.inContent = True

    def endElement (self, name):
        if name == 'item':
            self.inItem = False
        elif self.inItem:
            if name == 'title':
                self.line = "Title: " + self.theContent + "."
                #self.line = self.line.encode('utf-8')

                # To avoid Unicode trouble
                #print "<p><a href=" +
                self.inContent = False
                self.theContent = ""
            elif name == 'link':
                #print " Link: " + self.theContent + "."
                self.enlace += "<p><a href=" + self.theContent + ">" + self.line + "</a></p>"
                #print self.enlace.encode('utf-8')
                self.inContent = False
                self.theContent = ""
                self.line = ""

    def characters (self, chars):
        if self.inContent:
            self.theContent = self.theContent + chars

# Load parser and driver
def obtener_noticias ():
        #Load parser and driver
    theParser = make_parser()
    theHandler = myContentHandler()
    theParser.setContentHandler(theHandler)
    # Ready, set, go!
    listado = urllib2.urlopen("http://barrapunto.com/index.rss")
    #xmlFile = open(archivo,"r")
    theParser.parse(listado)
    return theHandler.enlace

#print "Parse complete"
