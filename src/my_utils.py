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
                if row[country_column].strip('" ') == country:
                    try:
                        # Append results to add number of fires
                        results.append(int(float(row[fires_column])))
                    except ValueError:
                        # If value cannot be converted to integers, skip
                        continue
                    # If the file cannot be found, terminate the function
    except FileNotFoundError:
        raise
    return results

def get_mean(numbers):
    """Returns the mean from an array of numbers

    Arguments
    -------------
    numbers: an array containing integers which we want to compute the mean for

    Returns
    ------------
    mean: Mean value of the given array of integers
    """
    if len(numbers) == 0:
        raise ValueError("The list of numbers is empty.")
    mean = sum(numbers) / len(numbers)
    return mean
    
def get_median(numbers):
    """Returns the median from an array of numbers

    Arguments
    -------------
    numbers: an array containing integers which we want to compute the median for

    Returns
    ------------
    mean: median value of the given array of integers
    """
    if len(numbers) == 0:
        raise ValueError("The list of numbers is empty.")
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    mid = n // 2
    if n % 2 == 0:
        # even number of elements → average the two middle values
        median = (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
    else:
        # odd number of elements → take the middle value
        median = sorted_nums[mid]
    return median

def get_sd(numbers):
    """Returns the standard deviation from an array of numbers

    Arguments
    -------------
    numbers: an array containing integers which we want to compute the standard deviation for

    Returns
    ------------
    sd: standard deviation of the given array of integers
    """
    if len(numbers) == 0:
        raise ValueError("The list of numbers is empty.")
    mean = sum(numbers) / len(numbers)
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    sd = (variance)**0.5
    return sd
                 
