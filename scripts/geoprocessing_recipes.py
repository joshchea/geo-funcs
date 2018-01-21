#----------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# Name:        geoprocessing_recipes
# Purpose:     These are some recipes for commonly performed gis functions like point in polygon, intersect etc... 
#               
# Author:      Chetan Joshi, Portland OR
#
# Dependencies:osgeo ogr library is required - pip install osgeo : for details see - https://pypi.python.org/pypi/GDAL
#
# Created:     01/20/2018
#              
# Copyright:   (c) Chetan Joshi 2018
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
from osgeo import ogr

def point_in_polygon(PointData,  ZoneWKTGeoms):
    '''Takes:
    
       PointData    = ["NO","XCOORD","YCOORD"]
       ZoneWKTGeoms = ["NO", "WKTSurface"]

       Returns:
       
       List with point ids and their container polygon id/no  
    '''
    POI_to_Zone = []
    for ZoneNo, Surface in ZoneWKTGeoms:
        Poly = ogr.CreateGeometryFromWkt(Surface)
        temp = []
        for no, x, y in PointData:
            point = ogr.Geometry(ogr.wkbPoint)
            point.AddPoint(x, y)
            if Poly.Contains(point):
                POI_to_Zone.append([no, ZoneNo])
            else:
                temp.append([no,x,y])
        PointData = temp
        
    return POI_to_Zone