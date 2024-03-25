import scanner
from interpreter import core_program_file, core_data_file

def initialize_tokenizer(core_file):
    tok = scanner.Scanner(core_file)
    return tok

def initialize_data(data_file):
    data = []
    with open(data_file, 'r') as file:
        for line in file:
            data.append(int(line.strip()))
    return data

global tokenizer, data_arr, data_idx
tokenizer = initialize_tokenizer(core_program_file)
data_arr = initialize_data(core_data_file)
data_idx = 0


