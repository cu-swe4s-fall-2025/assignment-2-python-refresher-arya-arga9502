#!/bin/bash

set -e

echo "Example 1 (works):"
python print_fires.py \
    --country "United States of America" \
    --country_column 0 \
    --fires_column 3 \
    --file_name Agrofood_co2_emission.csv \
    --operation "sd"

echo "Example 2 (missing file):"
python print_fires.py \
    --country "United States of America" \
    --country_column 0 \
    --fires_column 3 \
    --file_name NoFile.csv

echo "Example 3 (wrong column for country):"
python print_fires.py \
    --country "United States of America" \
    --country_column 10 \
    --fires_column 3 \
    --file_name Agrofood_co2_emission.csv