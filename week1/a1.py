num_list = [1, 5, 7, 15, 16, 22, 28, 29]

def get_odd_num(input_list):
    output_list = []
    for i in input_list:
        if i % 2 == 1 : output_list.append(i)
    return output_list

print(get_odd_num(num_list))