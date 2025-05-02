
# hori_block_2
# The Side of the hori_block_1
'''
Goal is to Generate Number that are not Similar to hori_block_1 in terms of horizontal 
to check it i need to 

hori_block_1 =  [7, 2, 9]
                [5, 8, 6]
                [3, 1, 4]

How to Access the List of 
print(hori_block_1)
'''

import random 
hori_block_1 = [1,2,3,4,5,6,7,8,9]
# print(hori_block_1[0:3]) # this is how i can access the first 3 Lines 




# Constraining the hori_block_2
'''
Instead of random.randint(1,9) because it took over i need it to make it relative man 
Maybe the Hierarchy of Constraint really matter to 
'''
# while len(hori_block_2) < 9:
#     random_num_2 = random.randint(1, 9) # This is a Keeping a generator 
#     if random_num_2 not in hori_block_2: # The Number should not be in hori_block_2
#         if random_num_2 != hori_block_1[0:3]: # in terms of picking a Number it needs to be not in the same line not in terms of each of it 
#             print(random_num_2)
#             if random_num_2 not in hori_block_1[0:3]:
#                 print(random_num_2)
#                 hori_block_2.append(random_num_2)
# print(hori_block_2)

sudoku_num = [1,2,3,4,5,6,7,8,9]
hori_block_2 = []
list_relative_horizontal = hori_block_1[0:3]
possible_num = []

'''I should print the Possible Num to reduce the random.randint Choices that depends on the line man'''

# Generating a Number in Relative to Sudoku_num
'''
list
0:3 
3:6 
6:9 
'''
list_relative_horizontal_2 = hori_block_1[0:3]
random_num = random.choice(list_relative_horizontal_2)
# print(random_num)





'''
This is Thinking Wrong maybe 
'''

