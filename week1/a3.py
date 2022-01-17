score = [(100, 100), (95, 90), (55, 60), (75, 80), (70, 70)]

def get_ave(input_score):
    i = 1
    for scores_per_student in input_score :
        average_score = sum(scores_per_student)/len(scores_per_student)
        print(f"No. {i}, Average score : {average_score}")
        i += 1

get_ave(score)
