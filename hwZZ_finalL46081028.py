#!/usr/bin/env python3

#### Functions for Q1
def weight_avg(input_filename, output_filename, w1=1, w2=1, w3=1, w4=1):
    with open(input_filename) as f:
        input_content = f.readlines()
    with open(output_filename, 'w') as fw:
        for each_line in input_content:
            serial_number, grade1_str, grade2_str, grade3_str, grade4_str = each_line.split(sep='  ')
            grade1 = float(grade1_str)
            grade2 = float(grade2_str)
            grade3 = float(grade3_str)
            grade4 = float(grade4_str)
            grade_average = ( grade1 * w1 + grade2 * w2 + grade3 * w3 + grade4 * w4 ) / (w1 + w2 + w3 + w4)
            fw.write(f'{serial_number} {grade_average:5.2f}\n')

#### Functions for Q2
def word_dict(input_filename, output_filename, sort_num=False):
    word_dict_content = dict()
    with open(input_filename) as f:
        input_string_list = f.readlines()
    input_word_list_nonstrip = []
    for input_string in input_string_list:
        input_string = input_string.split()
        input_word_list_nonstrip += input_string
    input_word_list = []
    for input_word in input_word_list_nonstrip:
        input_word = input_word.strip(' ,.!"\'-')
        input_word = input_word.lower()
        if input_word != "":
            input_word_list.append(input_word)
    longest_word_length = 0
    for item in input_word_list:
        word_dict_content[item] = word_dict_content.get(item, 0) + 1
        if len(item) > longest_word_length:
            longest_word_length = len(item)
    from collections import OrderedDict
    with open(output_filename,'w') as fw:
        if sort_num == True:   ## sort it by word
            word_dict_sorted_by_value = OrderedDict(sorted(word_dict_content.items(), key=lambda x: x[1], reverse=True))
            for i,j in word_dict_sorted_by_value.items():
                #print(f'{i:{longest_word_length}s}: {j}')
                fw.write(f'{i:{longest_word_length}s}: {j}\n')
        else:
            word_dict_sorted_by_key = OrderedDict(sorted(word_dict_content.items(), key=lambda x: x[0]))
            for i,j in word_dict_sorted_by_key.items():
                #print(f'{i:{longest_word_length}s}: {j}')
                fw.write(f'{i:{longest_word_length}s}: {j}\n')
 
if __name__ == '__main__':
    pass
