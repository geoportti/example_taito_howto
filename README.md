This repository is an example of using the computing services and the 
open data available in Taito in your research. The repository also works
as an example of sharing your code here at github

There are a lot of python libraries available at Taito already. In this
example we are using the fiona library to read GeoPackage file and calculate
the sum of the areas of the lake features. Unfortunately the available fiona
library does not support reading GeoPackage files, so we need to install a
newer version locally.

This can be done by creating a virtualenv in which we can install packages in
addition to the system-wide ones. First, create a new virtual environment.
