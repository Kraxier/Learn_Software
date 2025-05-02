'''
Goal Create another Box that are in the Right Side of the Main Box

or Create a Line of 3 box that are horizontal to Each Others 
'''
'''
list
0:3 
3:6 
6:9 
'''

import random 
hori_block_1 = [1,2,3,4,5,6,7,8,9]
hori_block_2 = []
hori_block_3 = []


# first_row_constraint = hori_block_1[0:3]
# second_row_constraint = hori_block_1[3:6]
# third_row_constraint = hori_block_1[6:9]
hori_block_1 = [1,2,3,4,5,6,7,8,9]
first_row_possible = hori_block_1[0:3]
second_row_possible = hori_block_1[3:6]
third_row_possible = hori_block_1[6:9]

# print(second_row_possible)
# print(third_row_possible)
# Connecting between the Random generator to a list 
while len(hori_block_2) < 3:
    random_num = random.choice(second_row_possible + third_row_possible)
    if random_num not in hori_block_2:
        hori_block_2.append(random_num)
# print("First Row is Done")
while len(hori_block_2) < 6:
    random_num = random.choice(first_row_possible + third_row_possible)
    if random_num not in hori_block_2:
        hori_block_2.append(random_num)
# print("Second Row is Done")
# print(hori_block_2)
while len(hori_block_2) < 9:
    available_choices = [n for n in (first_row_possible + second_row_possible) if n not in hori_block_2]
    if available_choices:
        random_num = random.choice(available_choices)
        hori_block_2.append(random_num)

print(hori_block_1)
print(hori_block_2)
    
    



# while len(hori_block_2) < 9:
#     # random_num = random.choice(second_row_possible and third_row_possible)
#     random_
#     if random_num not in hori_block_2:
#         hori_block_2.append(random_num)
#         print("It Append")
# print(hori_block_2)

# Random Number generator for hori_block_2
# random_num = random.choice(second_row_possible and third_row_possible)
# print(hori_block_1)
# print(random_num)

# while len(hori_block_2) < 9:
#     random_num = random.randint(1,9)
#     if random_num not in hori_block_2:
#         hori_block_2.append(random_num)
'''
basta bawal yung 1,2,3
'''


# while len(hori_block_2) < 9:
#     random_num = random.randint(1,9)
#     if random_num not in hori_block_2:
#         hori_block_2.append(random_num)



# list_relative_constraint_1 = hori_block_1[0:3]
# list_possible_num_1 = hori_block_1[3:9]

# while len(hori_block_2) < 3:
#     random_num = random.choice(list_possible_num_1)
#     if random_num not in hori_block_2:
#         hori_block_2.append(random_num)
# while len(hori_block_2) < 9:
#     random_num = random.randint(1,9)
#     if random_num not in hori_block_2:
#         hori_block_2.append(random_num)
# list_possible_num_2 = hori_block_2[3:9]

# print(hori_block_1)
# print(hori_block_2)


# Focus on Creating the hori_block_1 and hori_block_2
# while len(hori_block_3) < 3:
#     random_num = random.choice(list_possible_num_1 and list_possible_num_2)
#     if random_num not in hori_block_3:
#         hori_block_3.append(random_num)

# print(" ")
# print(hori_block_1)
# print(hori_block_2)
# print(hori_block_3)
# # while len(hori_block_3) < 9:
# #     random_num = random.randint(1, 9)
# #     if random_num not in hori_block_2:
# #         hori_block_3.append(random_num)
# # print(hori_block_3)


'''
Now i have a code to do this part the problem is the repetition of the code 


'''


