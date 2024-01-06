# TODO Напишите функцию find_common_participants
def find_common_participants(str1, str2, n=","):
    elements_in_str1 = list(str1.split(n))
    elements_in_str2 = list(str2.split(n))

    list_of_common_elements = list(set(elements_in_str1).intersection(elements_in_str2))
    list_of_common_elements.sort()
    return list_of_common_elements

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, "|"))
