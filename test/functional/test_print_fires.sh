test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest
run test_fires python src/print_fires.py \
    --country "United States of America" \
    --country_column 1 \
    --fires_column 4 \
    --file_name Agrofood_co2_emission_subset.csv \
    --operation "sd" \

assert_in_stdout "The number of fires were"
assert_exit_code 0
assert_in_stdout "Standard deviation of fires in United States of America:"

run test_error_no_file python src/print_fires.py \
    --country "United States of America" \
    --country_column 1 \
    --fires_column 4 \
    --file_name NoFile.csv \
    --operation "sd"

assert_in_stderr "Error: File 'NoFile.csv' not found."

run test_media python src/print_fires.py \
    --country "United States of America" \
    --country_column 1 \
    --fires_column 4 \
    --file_name Agrofood_co2_emission_subset.csv \
    --operation "median"

assert_in_stdout "Median number of fires in United States of America:"

run test_mean python src/print_fires.py \
    --country "United States of America" \
    --country_column 1 \
    --fires_column 4 \
    --file_name Agrofood_co2_emission_subset.csv \
    --operation "mean" \

assert_in_stdout "Mean number of fires in United States of America:"

