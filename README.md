<img src="https://github.com/geoportti/Logos/blob/master/geoportti_logo_300px.png">

# Example of calculating the total area of Finnish lakes using Taito
## Workflow
### 1. Prepare your environment
#### Python 3
There are a lot of python libraries available at Taito already. In this example
we are using the fiona library to read GeoPackage file and calculate the sum of
the areas of the lake features in Finland.

A comprehensive collection of Python 3 libraries can be accessed by loading a
module called "geoconda". This is done by issuing a command
```
module load geoconda
```
This will give you a Python 3.7 environment and the needed libraries.

#### Python 2
If you for some reason must use Python 2, loading the geoconda module is not an
option. One way forward is to instead load module "geo-env". This will give you
Python 2 environment and several libraries as well.
```
module load geo-env
```
Unfortunately the available fiona library does not support reading GeoPackage
files, so we need to install a newer version locally.  This can be done by
creating a virtualenv in which we can install packages in addition to the
system-wide ones. First, create a new virtual environment by typing the
following commands on Taito command prompt.
```
cd ~
mkdir venvs
virtualenv venvs/fiona_gpkg
```
Once the environment is created, activate it and install a newer fiona.
```
source venvs/fiona_gpkg/bin/activate
pip install --upgrade fiona
```
In the following it is assumed that the "geoconda" environment is used. Do not use the linked files but use the ones ending with "geoenv" instead.

### 2. Create your script and download it into Taito
The script [taito_LakeExample_script_geoconda.py](https://github.com/geoportti/example_taito_howto/blob/master/taito_LakeExample_script_geoconda.py)
sums the areas of all of the features in a given file and a layer. In this case the file *'MTK-vakavesi_19-01-23.gpkg'* contains two
layers, 'jarvi' (lake) and 'meri' (sea).

The script is written in such a way that it can be parallelized using the
'Array Job' functionality of the submit system used in Taito. If there are N
jobs launched, each job reads only M/N features, where M is the total number
of features in the layer. Therefore the script is launched with two argument:
the order of the job in the job array, and the total number of launched jobs.

In this example, with N jobs the jobs must be numbered from 0 to N-1.
In this example the analysis is so simple that most of the time is probably
used in reading the file. Therefore the parallelization may not provide
noticeable speedup.

Save the script file into your working directory on Taito.

### 3. Create a batch job script for running your code
The job is sent into the queue of Taito by a another script called the [batch job](https://github.com/geoportti/example_taito_howto/blob/master/LakeRun_geoconda.job)
The batch job file tells the queue system for example how many processes are requested and what is the estimated running time of the script.
In batch job it is essential that we load the required modules.
Save the batch job into your working directory on Taito.

### 4. Submit the job into the queue
Submit the job into the queue with the following command on Taito command prompt:
```
sbatch LakeRun_geoconda.job
```
The progress can be checked for example with the command:
```
squeue | grep <your username>
```
### 5. See your results
When the run is complete you can see the results in the batch output file in your working directory.

## Usage and Citing
When used, the following citing should be mentioned: "We made use of geospatial
data/instructions/computing resources provided by the Open Geospatial
Information Infrastructure for Research (oGIIR,
urn:nbn:fi:research-infras-2016072513) funded by the Academy of Finland."
