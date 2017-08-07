# GrADS Station Data Generator

This is a python script to generate binary station data for GrADS (Grid Analysis and Display System).
This script is based in C source code described in [documentation](http://cola.gmu.edu/grads/gadoc/aboutstationdata.html#station) of GrADS

```shell
Station data creator for GrADS

optional arguments:
  -h, --help            show this help message and exit
  --infile INFILE, -i INFILE
                        Input file, station data file
  --outfile OUTFILE, -o OUTFILE
                        Output file
  --latc LATC           Latitude column number [starts on 0]
  --lonc LONC           Longitude column number [starts on 0]
  --stidc STIDC         Station id column number [starts on 0]
  ```

## Exemple:

### Station data file:
```
Stid    Lat    Lon    Rainfall
QQQ    34.3  -85.5    123.3 
RRR    44.2  -84.5     87.1 
SSS    22.4  -83.5    412.8
TTT    33.4  -82.5     23.3 
QQQ    34.3  -85.5    145.1
RRR    44.2  -84.5    871.4
SSS    22.4  -83.5    223.1
TTT    33.4  -82.5     45.5
````

### Generating a binary station data:

```
python grads_station_data.py \
 -i station.txt \ #input file
 -o staion.dat \  #output file
 --latc=1 \       #number of lat column
 --lonc=2 \       #number of lon colunm
 --stidc=0        #number of station id colunm