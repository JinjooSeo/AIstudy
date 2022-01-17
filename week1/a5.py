inputs = "cat32dog16cow5"

def string_list(input_string):
    output_string = ""
    for i in input_string:
        if i.isdigit() : output_string += " "
        else : output_string += i

    output_list = output_string.split()
    return output_list

print(string_list(inputs))
