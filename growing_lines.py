def summary_ranges(listing):
    print(len(listing))
    list_of_ranges = []
    if len(listing) < 2:
        return list_of_ranges
    else:
        # start_position = 0
        # next_position = start_position + 1
        # while listing(start_position) == listing(start_position + 1) - 1:
        #     start_position += 1
        # for start_position in range(0,len(listing)-2):
        
        start_index = 0
        counter = 0
        while start_index <= len(listing) - 1:
           inner_index = start_index
           while (inner_index < len(listing) - 1) and (listing[inner_index] == listing[inner_index + 1] - 1):
              inner_index += 1
              counter += 1
           if counter > 0:
                list_of_ranges.append(f'{listing[start_index]} -> {listing[start_index+counter]}')
           counter = 0
           start_index = inner_index + 1
                
    return list_of_ranges


print(summary_ranges([1,2,3,4,7,8,10,-1,0,1,7,3,6,1,2]))
print(summary_ranges([1,2,3,4,7,9,10]))
