def fun3(prob_list: list) -> list:
    """
   возвращает лист только с нечетными индексами
   :param prob_list: list
   :return: list
   """
    prob_list2 = []
    for i in range(len(prob_list)):
        if i % 2 != 0:
            prob_list2.append(prob_list[i])
    prob_list = prob_list2
    return prob_list
