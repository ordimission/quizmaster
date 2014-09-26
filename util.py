import random

# shuffle function
def shuffle(source_array,target_size):
    target_array = []
    for i in range(0,target_size):
        target_array.append(source_array[i])
    for i in range(target_size,len(source_array)):
        j =  random.randint(0,i-1)
        if j < target_size:
	     target_array[j] = source_array[i]	
    return target_array


