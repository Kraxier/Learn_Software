import random

'''
Create a Reusable Function for Printing, Appending Numbers
'''

hori_block_1 = []

while len(hori_block_1) < 9:
    random_num_1 = random.randint(1, 9)
    if random_num_1 not in hori_block_1:
        hori_block_1.append(random_num_1)

# Printing it in 3x3 Grid
for i in range(0, len(hori_block_1), 3):
    print(hori_block_1[i:i+3])
