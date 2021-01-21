# Alphabet Soup Solution
# By Bethany Thompson
# 1/20/2021

def alphabetize_words(my_string):
    
    '''
    This functions accepts a string and returns the string sorted alphabetically
    by each word.
    '''

    # splitting string by spaces
    my_string_list = str.split(my_string)

    # initialzing variable as empty string to add the sorted words to
    my_string_sorted = ''

    # looping through each word in the string
    for x in range(0, len(my_string_list)):
    
        # resetting word to sorted word
        my_string_list[x] = sorted(my_string_list[x])
    
        # adding sorted word to new string
        if x != len(my_string_list):
        
            # only adding trailing space if not the last word in the string
            my_string_sorted += (''.join(my_string_list[x]) + ' ')
    
        else:
        
            # does not add trailing space because last word in the string
            my_string_sorted += (''.join(my_string_list[x]))
            
    return my_string_sorted