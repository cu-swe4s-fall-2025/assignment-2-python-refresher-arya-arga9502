def get_column(file_name, query_column, query_value, result_column):
    results = []
    with open(file_name, "r") as f:
        for line in f:
            row = line.rstrip().split(",")
            if row[query_column] == query_value:
                results.append(row[result_column])
    return results
