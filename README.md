### Fire Analysis Tool (v2.0.0)

## Description

This tool is used to extract the number of fires from a given country. The user is expected to define 4 arguments to the run the function successfully in the command line.

```bash
'file_name':      the path to the input file
'country_column': the column index where the country names are stored
'country':        the name of the country we want fire information from
'fires_column':  the column index where the desired values, i.e, number of fires are stored
```

---------------------------------------------------------------------------------
## Installation

1. Make sure you have **Python 3.7+** installed.  
   You can check with:
```bash
python --version
```
2. Clone this repository
```bash
git clone https://github.com/cu-swe4s-fall-2025/assignment-2-python-refresher-arya-arga9502.git
cd assignment-2-python-refresher-arya-arga9502.git
```


## Usage
Demo code to run the program
```bash
python print_fires.py --country "United States of America" --country_column 0 --fires_column 3 --file_name Agrofood_co2_emission.csv
```



## Testing

Unit tests and functional tests have been added in the test directory. These tests must be run from the root directory of the repository. 

The unit test has been written to test the functions defined in this package, i.e. functions to calculate of mean, median, and standard deviation. You will be able to run the unit test with the command: 

```bash
python src/test_my_utils.py
```
You functional test has been written to test whether the program as a whole runs correctly. You will be able to run the functional test with the command:

```bash
bash src/test_print_fires.py
```
