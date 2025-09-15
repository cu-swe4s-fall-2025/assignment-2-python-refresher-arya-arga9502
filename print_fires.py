"""
print_fires.py

Reads an input file and prints the number of fires for a given country.

Arguments:
    --country (str)         Name of the country
    --country_column (int)  Column index for country names
    --fires_column (int)    Column index for number of fires
    --file_name (str)       Path to the input file
"""
import my_utils
import argparse
import sys


def main():
    parser = argparse.ArgumentParser(
        description="Print number of fires for a given country."
        )
    parser.add_argument("--country", required=True, help="Country name")
    parser.add_argument("--country_column", type=int,
                        required=True, help="Column index for country names")
    parser.add_argument("--fires_column", type=int,
                        required=True, help="Column index for number of fires")
    parser.add_argument("--file_name",
                        required=True, help="Path to the input file")

    args = parser.parse_args()

    try:
        fires = my_utils.get_column(
            args.file_name,
            args.country_column,
            args.country,
            args.fires_column
        )
        print(f"The number of fires were {fires}.")
    except FileNotFoundError:
        print(f"Error: File '{args.file_name}' not found.", file=sys.stderr)
    except ValueError as e:
        print(f"Error: Could not convert values to integers. {e}",
              file=sys.stderr)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
