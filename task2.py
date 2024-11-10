
participants_first_group = "Иванов|Петров|Пушкин"
participants_second_group = "Петров|Сидоров|Смирнов"

common_sn = []

def find_common_participants(str_1, str_2, sep = '|'):
    str_1 = str_1.split(sep)
    str_2 = str_2.split(sep)
    for i in range(len(str_1)):
        for j in range(len(str_2)):
            if str_1[i] == str_2[j]:
                common_sn.append(str_1[i])
    return sorted(common_sn)

print(find_common_participants(participants_first_group, participants_second_group))