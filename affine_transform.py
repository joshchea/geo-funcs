#----------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# Name:        affine_transform
# Purpose:     Performs a general affine transformation from one Coordinate System to another.
#              Basically of the Type: X'-> aX + bY + e
#                                     Y'-> cX + dY + f
#              Where X' and Y' are for the new system of coordinates
#              This routine is useful for transforming networks from Synchro/Emme/Other tools that might contain older non-gis projection networks.
#              Expected usage is to obtain a,b,c,d,e,f values based on input of 3 xy coordinates from old system and corresponding points in the new system.
#              Once the networks are transformed, they can be used and re-projected just like other typical gis-based coordinate systems.
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

def transformCoords(x_A, y_A, x_B, y_B):
    '''Returns affine transform coefficients
         x_A = Three X's from Old System
         y_A = Thre Y's from Old System  } ex. synchro network

         x_B = Three X's from New System
         y_B = Three Y's from New System } ex. WGS (lat/lon) system

         usage:
         b,a,e,d,c,f = transformCoords(x_A, y_A, x_B, y_B)
         new_X = a*old_X + b*old_Y + e
         new_Y = c*old_X + d*old_Y + f
    '''
    
    b = ((x_B[2] - x_B[0])- ((x_A[2]-x_A[0])*(x_B[1]-x_B[0])/(x_A[1]-x_A[0])))/((y_A[2]-y_A[0]) -((x_A[2]-x_A[0])*(y_A[1]-y_A[0])/(x_A[1]-x_A[0])))

    a = ((x_B[1] - x_B[0]) - b*(y_A[1]-y_A[0]))/(x_A[1]-x_A[0])    
    
    e = x_B[0] - (a*x_A[0] + b*y_A[0])
    

    d = ((y_B[2] - y_B[0])- ((x_A[2]-x_A[0])*(y_B[1]-y_B[0])/(x_A[1]-x_A[0])))/((y_A[2]-y_A[0]) -((x_A[2]-x_A[0])*(y_A[1]-y_A[0])/(x_A[1]-x_A[0])))

    c = ((y_B[1] - y_B[0]) - d*(y_A[1]-y_A[0]))/(x_A[1]-x_A[0])    
    
    f = y_B[0] - (c*x_A[0] + d*y_A[0])

    return b,a,e,d,c,f

  

