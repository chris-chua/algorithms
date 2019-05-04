def average(array):
    # Use set to get the unique array: unique
    unique = set(array)

    # Calculate the average of the unique array
    average = sum(unique) / len(unique)

    # Return the result
    return(average)