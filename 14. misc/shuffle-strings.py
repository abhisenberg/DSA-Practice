def shuffle_list(input_list):
    # Make a copy of the input list to avoid modifying the original list
    shuffled_list = input_list[:]
    
    # Use the random.shuffle method to shuffle the list in place
    random.shuffle(shuffled_list)
    
    return shuffled_list

print(shuffle_list())