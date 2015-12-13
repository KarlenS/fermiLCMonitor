#!/usr/bin/python

import urllib2,requests
import argparse
from astropy.io import fits as pf
import numpy as np
from bs4 import BeautifulSoup
from time import gmtime, strftime
import matplotlib.pyplot as plt

class fermiLC(object):

    def __init__(self):

        self.date = strftime('%Y-%m-%d',gmtime())

    def getPageSource(self):
        fermiURL = 'http://fermi.gsfc.nasa.gov/ssc/data/access/lat/msl_lc/'
        return urllib2.urlopen(fermiURL)

    def getLCfits(self, url):
        fitsfile = pf.open(url)
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
            url = linkbase + link.get('href')
            lcDailyFile = lc.getLCfits(url)

            #opening up the fits file
            data_daily = lcDailyFile[1].data

            #grab the light curve
            start_time = data_daily['START']
            end_time = data_daily['STOP']
            flux_100_300000 = data_daily['FLUX_100_300000']
            error_100_300000 = data_daily['ERROR_100_300000']

            #calculate light curve parameters
            weights = np.divide(1.,error_100_300000)
            print data_daily['NAME'][0],np.average(flux_100_300000,weights=weights)

            #plotting the light curve,,,
            plt.errorbar(start_time,flux_100_300000,yerr=error_100_300000,fmt='o')
            plt.show()

            break
           
        if link.get_text() == 'Weekly Light Curve Fits File':
            url = linkbase + link.get('href')
            lcWeeklyfile = lc.getLCfits(url)

            #opening up the fits file
            data_daily = lcWeeklyFile[1].data
       
if __name__ == '__main__':
    main()
