from DS_course_Savenko_VS.Homework.Lesson_4_Project import (
    list_of_numbers2,
    list_of_numbers3,
    fun2,
    fun3,
    lst_in_str
)

file = open('Data\saves_processed_data.txt', 'w')
text_2 = lst_in_str(fun2(list_of_numbers2())) + '  '
text_3 = lst_in_str(fun3(list_of_numbers3())) + '  '
file.write(text_2)
file.write(text_3)
file.close()

# %%
