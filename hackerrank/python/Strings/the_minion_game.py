def minion_game(string):
    vowels = 'AEIOU'

    # Initialize both scores: stuart_score and kevin_score
    stuart_score = 0
    kevin_score = 0
    
    # Loop through string to check if character is a vowel
    for i in range(len(string)):
        if string[i] in vowels:
            kevin_score += len(string) - i
        else:
            stuart_score += len(string) - i
  
    # Print results
    if kevin_score > stuart_score:
        print('Kevin {}'.format(kevin_score))
    elif stuart_score > kevin_score:
        print('Stuart {}'.format(stuart_score))
    else:
        print('Draw')