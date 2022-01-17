sentence = "way a is there will a is ther Where"

def reverse_sentence(input_sentence):
    output_sentence = "" #initialization 
    whole_rev_list = input_sentence.split() #split the word
    for word in reversed(whole_rev_list) : #reverse the order
        output_sentence += word 
        if word is whole_rev_list[0] : continue # skip the adding space if the sentence is end
        output_sentence += " "
    return output_sentence

print(reverse_sentence(sentence))