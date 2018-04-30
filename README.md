# geo-funcs
Some utilities for geo spatial operations in python. This a an evolving set of python scripts for performing gis/geo operations on spatial data. The scripts cover functionalities such as - point in polygon test, generation of interpolated trajectories from GTFS data, affine transformation for transforming networks in generic coordinate systems to true gis systems etc. A good reference for getting familiar with GDAL is Chris Garrard's tutorials posted here: http://www.gis.usu.edu/~chrisg/python/2009/

Dependencies include (these libraries may not be natively installed with Python): 
<ul style="list-style-type:disc">
  <li>osgeo ogr library (https://trac.osgeo.org/gdal/wiki/GdalOgrInPython)</li>
  <li>numpy library (http://www.numpy.org/)</li>
  <li>sqlite3 library (https://docs.python.org/2/library/sqlite3.html) {this may or may not come with a given python install - better to check by trying an import sqlite3 in python console to confirm}</li>
</ul> 


 
