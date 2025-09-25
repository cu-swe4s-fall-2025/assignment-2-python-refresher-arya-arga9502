#!/bin/bash

set -e

echo "Example 1 (works):"
python src/print_fires.py \
    --country "United States of America" \
    --country_column 1 \
    --fires_column 4 \
    --file_name Agrofood_co2_emission_subset.csv \
    --operation "sd"

echo "Example 2 (missing file):"
python src/print_fires.py \
    --country "United States of America" \
    --country_column 1 \
    --fires_column 4 \
    --file_name NoFile.csv

echo "Example 3 (wrong column for country):"
python src/print_fires.py \
    --country "United States of America" \
    --country_column 2 \
    --fires_column 4 \
    --file_name Agrofood_co2_emission_subset.csv