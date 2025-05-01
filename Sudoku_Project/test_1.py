import random

'''
Create a Reusable Num Generator DONE
Create a Sudoku 3x3 Grid Block DONE
Figure out the Damn Logics for Building the Sudoku 
'''



# while len(hori_block_1) < 9:
#     random_num_1 = random.randint(1, 9)
#     if random_num_1 not in hori_block_1:
#         hori_block_1.append(random_num_1)


def num_generator():
    random_num = random.randint(1, 9)
    return random_num
# g = num_generator()
# print(g)
# Printing it in 3x3 Grid
def print_block_sudoku(sudoku_block):
    for i in range(0, len(sudoku_block), 3):
        print(sudoku_block[i:i+3])
# print_block_sudoku(hori_block_1)

hori_block_1 = []
hori_block_2 = []
verti_block_1 = []

while len(hori_block_1) < 9:
    num_1 = num_generator()
    if num_1 not in hori_block_1:
        hori_block_1.append(num_1)

print_block_sudoku(hori_block_1)

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

# verti_block_1
# The bottom of the hori_block_1

