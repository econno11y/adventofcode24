from utils.get_inputs import inputs


def count_word(row, word='XMAS'):
    # count all instances of word in a row
    count = 0
    for letter in range(len(row) - len(word) + 1):
        if row[letter:letter + len(word)] == word:
            count += 1
    return count


file = inputs(4)
xmas_count = 0

# get a list of rows
rows = [line.strip() for line in file]
height = len(rows)
width = len(rows[0])

# get a list of columns
columns = []

for column_index in range(width):
    # add a new column to the list of columns
    columns.append('')
    # iterate through the rows and add the letter at the current column index
    for row_index in range(height):
        columns[column_index] += rows[row_index][column_index]


def fill_left_diagonal(column_index, row_index=0):
    left_diagonal = ''
    
    while row_index < height and column_index > -1:
        left_diagonal += rows[row_index][column_index]
        
        # move down one row and left one column
        row_index += 1
        column_index -= 1
        
    return left_diagonal
    

def fill_right_diagonal(column_index, row_index=0):
    right_diagonal = ''
    
    while row_index < height and column_index < width:
        right_diagonal += rows[row_index][column_index]
        
        # move down one row and right one column
        row_index += 1
        column_index += 1
        
    return right_diagonal   
    
    
# get the list of left diagonals
left_diagonals = []
# ================================
#      |X|M|A|S|T|E|R|S|T|
#    |M|A|S|T|E|R|S|T|A|
#  |A|S|T|E|R|S|T|A|M|
# |S|T|E|R|S|T|A|M|A|
# ================================

# index of the last letter in XMAS
len_xmas = len('XMAS')

# get all the left diagonals that start in the first row
for i in range((len_xmas - 1), width):
    left_diagonals.append(fill_left_diagonal(column_index=i))
    
    
# get all the left diagonals that start in the first column
for i in range(1, height - len_xmas):
    left_diagonals.append(fill_left_diagonal(row_index=i, column_index=width - 1))
      

# get the list of right diagonals
right_diagonals = []
# ================================
# |S|T|E|R|S|T|A|M|A|
#   |A|S|T|E|R|S|T|A|M|
#     |M|A|S|T|E|R|S|T|A|
#       |X|M|A|S|T|E|R|S|T|
# ================================

# get all the right diagonals that start in the first row
for i in range(width - len_xmas):
    right_diagonals.append(fill_right_diagonal(column_index=i))

# get all the right diagonals that start in the first column
for i in range(1, height - len_xmas):
    right_diagonals.append(fill_right_diagonal(row_index=i, column_index=0))

       
# list of all 2D arrays
two_d_arrays = [rows, columns, left_diagonals, right_diagonals]
# count all instances of XMAS in the forws
for two_d_array in two_d_arrays:
    for list_of_letters in two_d_array:
        xmas_count += count_word(list_of_letters, 'XMAS')
        xmas_count += count_word(list_of_letters, 'SAMX')
        
print(xmas_count)
    
                  

    
