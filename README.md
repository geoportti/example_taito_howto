<img src="https://github.com/geoportti/example_taito_howto/blob/master/geoportti_logo_484px.png" width="300">

# Example of calculating the total area of Finnish lakes using Taito
## Workflow
### 1. Install needed libraries for your script
There are a lot of python libraries available at Taito already. In this
example we are using the fiona library to read GeoPackage file and calculate
the sum of the areas of the lake features in Finland. 
Unfortunately the available fiona library does not support reading GeoPackage files, 
so we need to install a newer version locally.
This can be done by creating a virtualenv in which we can install packages in
addition to the system-wide ones. First, create a new virtual environment by typing 
the following commands on Taito command prompt.
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
### 2. Create your script and download it into Taito
The script [taito_LakeExample_script.py](https://github.com/geoportti/example_taito_howto/blob/master/taito_LakeExample_script.py)
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
The job is sent into the queue of Taito by a another script called the [batch job](https://github.com/geoportti/example_taito_howto/blob/master/LakeRun.job.txt).
Batch Job tells the queue for example system how many jobs is requested and what is the estimated running time of the script.
In batch job it is essential that we load the required modules and activate the virtual environment.
Save the batch job into your working directory on Taito.

### 4. Submit the job into the queue

Submit the job into the queue with the following command on Taito command prompt:
```
sbatch LakeRun.job
```
The progress can be checked for example with the command:
```
squeue | grep <your username>
```
### 5. See your results
When the run is complete you can see the results in the batch output file in your working directory.

## Usage and Citing
When used, the following citing should be mentioned:
"We made use of geospatial data/computing resources provided by the Open Geospatial Information Infrastructure for Research (oGIIR, urn:nbn:fi:research-infras-2016072513) funded by the Academy of Finland."
 
