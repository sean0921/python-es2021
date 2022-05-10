#!/usr/bin/env python3

input_filename_A = './hw11_material/matrixA.txt'
input_filename_B = './hw11_material/matrixB.txt'
output_filename  = './hw11_material/matrixout.txt'

#####################

def raw_matrix_line_to_sparse(raw_matrix_line: str):
    import collections
    import string
    smatrix_line = collections.defaultdict(int)
    matrix_list = raw_matrix_line.split()
    col_length = len(matrix_list)
    for index,item in enumerate(matrix_list):
        if int(item) == 0:
            continue
        else:
            smatrix_line[index] = int(item)
    smatrix_line = dict(smatrix_line)
    return(smatrix_line, col_length)

#print(raw_matrix_line_to_sparse('    0     0    123    0'))

def raw_matrix_to_sparse(raw_matrix_list: list):
    smatrix_dict = {}
    smatrix_dict_content = {}
    row_length = len(raw_matrix_list)
    for index,item in enumerate(raw_matrix_list):
        each_line_dict, col_length = raw_matrix_line_to_sparse(item)
        for keys in each_line_dict.keys():
            smatrix_dict_content[(index,keys)] = each_line_dict[keys]
        smatrix_dict['size'] = (row_length, col_length)
        smatrix_dict['content'] = smatrix_dict_content
    return(smatrix_dict)

#print(raw_matrix_to_sparse(['    0     0   2    0','1 0 0 0','0 0 5 0', '3 0 0 0', '0  1 0 0']))

def sparse_to_dense(sparse_matrix):
    dim_row = sparse_matrix['size'][0] 
    dim_col = sparse_matrix['size'][1]
    matrix_out = []
    for i in range( 0, dim_row ):
        matrix_out.append([])
        for m in range( 0, dim_col ):
            matrix_out[i].append(0)
    #print(matrix_out)
    for i in list(sparse_matrix['content'].keys()):
        #print(sparse_matrix['content'][i])
        matrix_out[i[0]][i[1]] = sparse_matrix['content'][i]
    return matrix_out

def is_valid_2d_matrix(input_list: list) -> bool:
    if type(input_list) != list:
        return False
    for i in range(0,len(input_list)):
        if len(input_list[i] != input_list[0]):
            return False
        if len(input_list[i][0]) != 1:
            return False
    return True

def check_outer_product_available(matrix_list_1: list, matrix_list_2: list) -> bool:
    if ( not is_valid_2d_matrix(matrix_list_1) ) or ( not is_valid_2d_matrix(matrix_list_2) ):
        return False
    if len(matrix_list_1[0]) != len(matrix_list_2):
        return False
    return True

def matrix_outer_product(matrix_list_1: list, matrix_list_2: list) -> list:
    # 先產生 size 對的空陣列並且補 0
    matrix_result = []
    for i in range( 0, len(matrix_list_1) ):
        matrix_result.append([])
        for m in range( 0, len(matrix_list_2[0]) ):
            matrix_result[i].append(0)
    for i in range( 0, len(matrix_list_1) ):
        for j in range( 0, len(matrix_list_1[i]) ):
            for m in range( 0, len(matrix_list_2[0]) ):
                matrix_result[i][m] += matrix_list_1[i][j] * matrix_list_2[j][m]
    return matrix_result

def sparse_matrix_outer_product(sparse_matrix_1: dict, sparse_matrix_2: dict):
    dence_matrix_1 = sparse_to_dense(sparse_matrix_1)
    dence_matrix_2 = sparse_to_dense(sparse_matrix_2)
    dence_matrix_result = matrix_outer_product(dence_matrix_1,dence_matrix_2)
    #sparse_matrix_result = 
    return dence_matrix_result

with open(input_filename_A) as fa:
    fa_lines_list = fa.readlines()
    fa_smatrix = raw_matrix_to_sparse(fa_lines_list)
    del(fa_lines_list)

with open(input_filename_B) as fb:
    fb_lines_list = fb.readlines()
    fb_smatrix = raw_matrix_to_sparse(fb_lines_list)
    del(fb_lines_list)

#print(fa_smatrix)
#print(sparse_to_dense(fa_smatrix))
#print(fb_smatrix)
#print(sparse_to_dense(fb_smatrix))

with open(output_filename, 'w') as fo:
    output_matrix_list = sparse_matrix_outer_product(fa_smatrix, fb_smatrix)
    for i in output_matrix_list:
        for ii in i:
            fo.write(f'{ii}   ')
        fo.write('\n')

#############################################

import string

with open('Caesar_cipher_test.txt') as f:
    content = f.readlines()

moved_digit = int(content[0])
encrypted_text = content[1]

# a: 0, z: 25
#alphabet_dict = dict(zip(list(string.ascii_lowercase),range(0,26)))
#alphabet_dict_encrypted = {}
alphabet_list = list(string.ascii_lowercase)
encrypted_alphabet_list = [''] * 26
for i in range(0,26):
    encrypted_alphabet_list[ ( i + moved_digit) % 26 ] = alphabet_list[i]

decrypted_text = ''

for index,text in enumerate(list(encrypted_text)):
    if string.ascii_lowercase.find(text) > -1:
        decrypted_text += encrypted_alphabet_list[string.ascii_lowercase.find(text)]
    else:
        decrypted_text += text

print(decrypted_text)
