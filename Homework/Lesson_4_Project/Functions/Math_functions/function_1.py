def fun1(prob_list: list) -> list:
    """
    сортировка пузырьком
    """
    for j in range(len(prob_list)):
        for i in range(len(prob_list) - j - 1):
            if prob_list[i] > prob_list[i + 1]:
                a = prob_list[i]
                prob_list[i] = prob_list[i + 1]
                prob_list[i + 1] = a
    return prob_list
