'''
Sudoku Generator 

How to Run it 
python script_name.py


Generator Sudoku No. 
1. Create a Random Number in a rown
2. 

'''


import random

hori_block_1 = []
hori_block_2 = []
hori_block_3 = []
hori_block_4 = []
hori_block_5 = []
hori_block_6 = []
hori_block_7 = []
hori_block_8 = []
hori_block_9 = []

while len(hori_block_1) < 9:
    random_num_1 = random.randint(1, 9)
    if random_num_1 not in hori_block_1:
        hori_block_1.append(random_num_1)

print(hori_block_1)

scanner = 0 
#scanner_by_3_v1 = 0
#scanner_by_3_v2 = 3

#while len(hori_block_2) < 9:
#    random_num_2 = random.randint(1, 9)
#    print('im Stuck at 2 ')
#    if random_num_2 not in hori_block_2 and random_num_2 not in hori_block_1[scanner_by_3_v1:scanner_by_3_v2]:
#        hori_block_2.append(random_num_2)
#        scanner += 1
#        if scanner == 3:
#            #print("yeah bebe")
#            scanner_by_3_v1 += 3
#            scanner_by_3_v2 += 3
#        if scanner == 6:
#            #print("yeah bebe")
#            scanner_by_3_v1 += 3
#            scanner_by_3_v2 += 3
#        if scanner == 9:
#            #print("yeah bebe")
#            scanner_by_3_v1 += 3
#            scanner_by_3_v2 += 3
#print(hori_block_2)

#scanner_3rd = 0
#scanner_by_3_v1_3rd = 0
#scanner_by_3_v2_3rd = 3

#while len(hori_block_3) < 9:
#    random_num_3 = random.randint(1, 9)
#    print('im Stuck at 3 ')
#    #print("Currently at Third Block randoming Numbers ")
#    if random_num_3 not in hori_block_3 and random_num_3 not in hori_block_2[scanner_by_3_v1_3rd:scanner_by_3_v2_3rd] and random_num_3 not in hori_block_1[scanner_by_3_v1_3rd:scanner_by_3_v2_3rd] :
#        hori_block_3.append(random_num_3)
#        scanner_3rd += 1
#        #print(scanner_3rd)
#        if scanner_3rd == 3:
#            #print("yeah bebe")
#            scanner_by_3_v1_3rd += 3
#            scanner_by_3_v2_3rd += 3
#        if scanner_3rd == 6:
#            #print("yeah bebe")
#            scanner_by_3_v1_3rd += 3
#            scanner_by_3_v2_3rd += 3
#        if scanner_3rd == 9:
#            #print("yeah bebe")
#            scanner_by_3_v1_3rd += 3
#            scanner_by_3_v2_3rd += 3

#print(hori_block_3)

#scanner_4th = 0
#scanner_by_4_v1_4th = 0
#scanner_by_4_v2_4th = 3

#while len(hori_block_4) < 9:
#    random_num_4 = random.randint(1, 9)
#    print('im Stuck at 4 ')
#    if random_num_4 not in hori_block_4 and random_num_4 not in hori_block_1[scanner_by_4_v1_4th:scanner_by_4_v2_4th]:
#        hori_block_4.append(random_num_4)
#        scanner_4th += 1
#        if scanner_4th == 3:
#            scanner_by_4_v1_4th += 3
#            scanner_by_4_v2_4th += 3
#        if scanner_4th == 6:
#            scanner_by_4_v1_4th += 3
#            scanner_by_4_v2_4th += 3
#        if scanner_4th == 9:
#            scanner_by_4_v1_4th += 3
#            scanner_by_4_v2_4th += 3

#print(hori_block_4)

#scanner_5th = 0
#scanner_by_4_v1_5th = 0
#scanner_by_4_v2_5th = 3

#while len(hori_block_5) < 9:
#    random_num_5 = random.randint(1, 9)
#    print('im Stuck at 5 ')
#    if random_num_5 not in hori_block_5 and random_num_5 not in hori_block_4[scanner_by_4_v1_5th:scanner_by_4_v2_5th]:
#        hori_block_5.append(random_num_5)
#        scanner_5th += 1
#        if scanner_5th == 3:
#            scanner_by_4_v1_5th += 3
#            scanner_by_4_v2_5th += 3
#        if scanner_5th == 6:
#            scanner_by_4_v1_5th += 3
#            scanner_by_4_v2_5th += 3
#        if scanner_5th == 9:
#            scanner_by_4_v1_5th += 3
#            scanner_by_4_v2_5th += 3

#print(hori_block_5)

#scanner_6th = 0
#scanner_by_4_v1_6th = 0
#scanner_by_4_v2_6th = 3

#while len(hori_block_6) < 9:
#    random_num_6 = random.randint(1, 9)
#    print('im Stuck at 6 ')
#    if random_num_6 not in hori_block_6 and random_num_6 not in hori_block_4[scanner_by_4_v1_6th:scanner_by_4_v2_6th] and random_num_6 not in hori_block_5[scanner_by_4_v1_6th:scanner_by_4_v2_6th]:
#        hori_block_6.append(random_num_6)
#        scanner_6th += 1
#        if scanner_6th == 3:
#            scanner_by_4_v1_6th += 3
#            scanner_by_4_v2_6th += 3
#        if scanner_6th == 6:
#            scanner_by_4_v1_6th += 3
#            scanner_by_4_v2_6th += 3
#        if scanner_6th == 9:
#            scanner_by_4_v1_6th += 3
#            scanner_by_4_v2_6th += 3

#print(hori_block_6)

#scanner_7th = 0
#scanner_by_4_v1_7th = 0
#scanner_by_4_v2_7th = 3

#while len(hori_block_7) < 9:
#    random_num_7 = random.randint(1, 9)
#    print('im Stuck at 7 ')
#    if random_num_7 not in hori_block_7 and random_num_7 not in hori_block_4[scanner_by_4_v1_7th:scanner_by_4_v2_7th]:
#        hori_block_7.append(random_num_7)
#        scanner_7th += 1
#        if scanner_7th == 3:
#            scanner_by_4_v1_7th += 3
#            scanner_by_4_v2_7th += 3
#        if scanner_7th == 6:
#            scanner_by_4_v1_7th += 3
#            scanner_by_4_v2_7th += 3
#        if scanner_7th == 9:
#            scanner_by_4_v1_7th += 3
#            scanner_by_4_v2_7th += 3

#print(hori_block_7)

#scanner_8th = 0
#scanner_by_4_v1_8th = 0
#scanner_by_4_v2_8th = 3

#while len(hori_block_8) < 9:
#    random_num_8 = random.randint(1, 9)
#    print('im Stuck at 8 ')
#    if random_num_8 not in hori_block_8 and random_num_8 not in hori_block_7[scanner_by_4_v1_8th:scanner_by_4_v2_8th]:
#        hori_block_8.append(random_num_8)
#        scanner_8th += 1
#        if scanner_8th == 3:
#            scanner_by_4_v1_8th += 3
#            scanner_by_4_v2_8th += 3
#        if scanner_8th == 6:
#            scanner_by_4_v1_8th += 3
#            scanner_by_4_v2_8th += 3
#        if scanner_8th == 9:
#            scanner_by_4_v1_8th += 3
#            scanner_by_4_v2_8th += 3

#print(hori_block_8)

#scanner_9th = 0
#scanner_by_4_v1_9th = 0
#scanner_by_4_v2_9th = 3

#while len(hori_block_9) < 9:
#    random_num_9 = random.randint(1, 9)
#    print('im Stuck at 9 ')
#    if random_num_9 not in hori_block_9 and random_num_9 not in hori_block_7[scanner_by_4_v1_9th:scanner_by_4_v2_9th] and random_num_9 not in hori_block_8[scanner_by_4_v1_9th:scanner_by_4_v2_9th]:
#        hori_block_9.append(random_num_9)
#        scanner_9th += 1
#        if scanner_9th == 3:
#            scanner_by_4_v1_9th += 3
#            scanner_by_4_v2_9th += 3
#        if scanner_9th == 6:
#            scanner_by_4_v1_9th += 3
#            scanner_by_4_v2_9th += 3
#        if scanner_9th == 9:
#            scanner_by_4_v1_9th += 3
#            scanner_by_4_v2_9th += 3

#print(hori_block_9)
#print("")
# Store all the blocks in a list
#hori_blocks = [hori_block_1, hori_block_2, hori_block_3, hori_block_4, hori_block_5, hori_block_6, hori_block_7, hori_block_8, hori_block_9]

# Printing the 9x9 Sudoku grid
#for i in range(9):
#    # Print values in 3x3 chunks
#    print(f"{hori_blocks[i][0:3]} | {hori_blocks[i][3:6]} | {hori_blocks[i][6:9]}")
#    
#    # Add space after every third row to separate the 3x3 grids
#    if (i + 1) % 3 == 0 and i != 8:
#        print("-" * 21)  # Separator between blocks