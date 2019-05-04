def count_substring(string, sub_string):
    # initializing: count
    count = 0

    # looping through the whole string to check for sub_string
    for i in range(len(string)):
        if sub_string == string[i:i+len(sub_string)]:
            count += 1
            
    return count