#!/usr/bin/python

import urllib2
import argparse
from astropy.io import fits as pf
from bs4 import BeautifulSoup
from time import gmtime, strftime

class fermiLC(object):

    def __init__(self):

        self.date = strftime('%Y-%m-%d',gmtime())

    def getPageSource(self):
        fermiURL = 'http://fermi.gsfc.nasa.gov/ssc/data/access/lat/msl_lc/'
        return urllib2.urlopen(fermiURL)

    #def getAllLinks(self)

    def downloadLCfits(self, url):
        fitsfile = wget.download(url)
        return fitsfile

    #def calcBaseline(self):

    #def setBaseline(self):

    #def getFluxDiff(self):


def main():

    #parsing arguments
    parser = argparse.ArgumentParser(description='Checks the official Fermi-LAT light curves for signs of variability')
    parser.add_argument('--cuts', nargs='?', default='daily', help="Takes either 'daily' or 'weekly' for medium or soft analysis")
    args = parser.parse_args()


    lc = fermiLC()
    page = lc.getPageSource()
    soup = BeautifulSoup(page.read(),"lxml")

    linkbase = 'http://fermi.gsfc.nasa.gov'

    for link in soup.find_all('a'):
        if link.get_text() == 'Daily Light Curve Fits File':
            print 'found daily'
            #url = linkbase + link.get('href'))
            #lcDailyFile = lc.downloadLCfits(url)
            #need to break things out for each source
        if link.get_text() == 'Weekly Light Curve Fits File':
            #url = linkbase + link.get('href'))
            #lcWeeklyfile = lc.downloadLCfits(url)
            print 'found weekly'
       
       # if (link.get('href')[0:6]) == 'source':
       #     print "Source: ", link.get('href')[7:]
        #check to see if the source
        #if so grab the 


if __name__ == '__main__':
    main()
