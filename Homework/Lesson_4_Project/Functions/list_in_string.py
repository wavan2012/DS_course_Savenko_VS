def lst_in_str(prob_list: list) -> str:
    prob_str = "[" + str(prob_list[0])
    for i in range(1, len(prob_list)):
        prob_str += ', ' + str(prob_list[i])
    prob_str += "]"
    return prob_str
