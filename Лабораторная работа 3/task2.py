# TODO Напишите функцию find_common_participants
def find_common_participants(participants_str1, participants_str2, divider=","):
    participants_set1=set(participants_str1.split(divider))
    participants_set2 = set(participants_str2.split(divider))
    common_participants=list(participants_set1.intersection(participants_set2))
    common_participants.sort()
    return common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, "|" ))
# TODO Провеьте работу функции с разделителем отличным от запятой
