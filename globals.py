import scanner

global tokenizer
tokenizer = None

global data_arr
data_arr = []

global data_idx
data_idx = 0

def initialize_globals(core_program_file, data_file):
    global tokenizer
    tokenizer = scanner.Scanner(core_program_file)

    global data_arr
    with open(data_file, 'r') as file:
        for line in file:
            data_arr.append(int(line.strip()))

