# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 08:46:34 2019

"""

import sys

# Bug: when searching the libraries, the virtual environment must be searched
# before the libraries that are installed system-wide.
sys.path.insert(0, sys.path[-1])

import fiona
import shapely.geometry

gpkg_file = '/proj/ogiir-csc/mml/maastotietokanta/2019/MTK-vakavesi_19-01-23.gpkg'
my_rank = int(sys.argv[1])
N_procs = int(sys.argv[2])

sum_area = 0

with fiona.open(gpkg_file, 'r', driver='GPKG', layer='jarvi') as f:
    N_features = len(f) # The number of features in the file.
    N_features_per_proc = int(N_features / N_procs)
    index_start = my_rank * N_features_per_proc
    index_stop = index_start + N_features_per_proc
    # Make sure that the last feature is also read.
    if my_rank == N_procs - 1:
        index_stop = N_features
    # Read all the features that are assigned to this job, and sum up the
    # areas.
    for item in f.items(index_start, index_stop):
        s = shapely.geometry.shape(item[1]['geometry'])
        sum_area += s.area

# Write the sum into a file. Each job must write to a separate file.
outfile = 'sum_area_{}.txt'.format(my_rank)
with open(outfile, 'w') as f:
    f.write('Processed features [{}...{}[.\n'.format(index_start, index_stop))
    f.write('The sum of the areas: {:0.3f} km^2.\n'.format(sum_area / 1e6))


# The job is sent into the queue by a another script, which tells the queue
# for example system how many jobs is requested. Here it is essential that we
# load the required modules and activate the virtual environment.
