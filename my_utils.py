"""Functions to extract desired information for a given country

* get_column - returns the number of fires for a given country as integers

"""


def get_column(file_name, country_column, country, fires_column):
    """Extracts the number of fires for a given country from an input file.

    Arguments
    -------------
    file_name:      the path to the input file
    country_column: the column index where the country names are stored
    country:        the name of the country we want fire information for
    fires_column:  the column index where the desired values are stored

    Returns
    ------------
    results: The number of fires from a given country as a list of integers

    """

    results = []  # Initialize an empty list to store the number of fires
    try:
        with open(file_name, "r") as file:  # Read the input file
            for line in file:  # Iterate over each line
                # Remove trailing newline, split by comma into list of values
                row = line.rstrip().split(",")
                # If the input country matches country index, proceed
                if row[country_column] == country:
                    try:
                        # Append results to add number of fires
                        results.append((row[fires_column]))
                    except ValueError:
                        # If value cannot be converted to integers, skip
                        continue
                    # If the file cannot be found, terminate the function
    except FileNotFoundError:
        raise
    return results
