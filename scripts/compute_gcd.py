#----------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# Name:        compute_gcd
# Purpose:     Calculates great circle distance between given lat/lon coordinates. 
#               
# Author:      Chetan Joshi, Portland OR
# Dependencies:None
# Created:     01/20/2018
#              
# Copyright:   (c) Chetan Joshi 2015
# Licence:     Permission is hereby granted, free of charge, to any person obtaining a copy
#              of this software and associated documentation files (the "Software"), to deal
#              in the Software without restriction, including without limitation the rights
#              to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#              copies of the Software, and to permit persons to whom the Software is
#              furnished to do so, subject to the following conditions:
#
#              The above copyright notice and this permission notice shall be included in all
#              copies or substantial portions of the Software.
#
#              THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#              IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#              FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#              AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#              LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#              OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#              SOFTWARE.
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------#
from math import *

def computeGCD(lat1,lon1,lat2,lon2):
    #computes great circle distance from lat/lon
    '''lat1/lon1 = lat/lon of first pt
       lat2/lon2 = lat/lon of second pt
    '''
    degRad = pi/180
    lat1 = degRad*lat1
    lon1 = degRad*lon1
    lat2 = degRad*lat2
    lon2 = degRad*lon2
    dellambda = lon2-lon1 
    Numerator = sqrt((cos(lat2)*sin(dellambda))**2 + (cos(lat1)*sin(lat2)- sin(lat1)*cos(lat2)*cos(dellambda))**2)
    Denominator = sin(lat1)*sin(lat2) + cos(lat1)*cos(lat2)*cos(dellambda)
    delSigma = atan2(Numerator,Denominator)

    return 3963.19059*delSigma

  

