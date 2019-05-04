def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        # Initialize each k-length substring
        substring = ''
        # If next character is not in substring -> add to substring
        for j in range(k):
            if string[i+j] not in substring:
                substring += string[i+j]
        # Print substring
        print(substring)