# geo-funcs
Some utilities for geo spatial operations in python. This a an evolving set of python scripts for performing gis/geo operations on spatial data. The scripts cover functionalities such as - point in polygon test, generation of interpolated trajectories from GTFS data, affine transformation for moving networks in generic coordinate systems to true gis systems etc. 

Dependencies include (these libraries are not natively installed with Python): 
> osgeo ogr library (https://trac.osgeo.org/gdal/wiki/GdalOgrInPython)
> numpy library (http://www.numpy.org/)
> sqlite3 library (https://docs.python.org/2/library/sqlite3.html) {this may or may not come with a given python install - better to check by trying an import sqlite3 in python console to confirm} 
