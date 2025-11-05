def list_superset(list_set_1, list_set_2):
    if len(list_set_1) > len(list_set_2):
        count_of_matches = 0
        for i in range(len(list_set_2)):
            for j in range(len(list_set_1)):
                if list_set_1[j] == list_set_2[i]:
                    count_of_matches += 1
                    break
        if count_of_matches == len(list_set_2):
            return f'Набор{list_set_1} - супермножество.'
        else:
            return f'Супермножество не обнаружено.'       
    elif len(list_set_1) < len(list_set_2):
        count_of_matches = 0
        for i in range(len(list_set_1)):
            for j in range(len(list_set_2)):
                if list_set_1[i] == list_set_2[j]:
                    count_of_matches += 1
                    break
        if count_of_matches == len(list_set_1):
            return f'Набор{list_set_2} - супермножество.'
        else:
            return f'Супермножество не обнаружено.'
    else:
        count_of_matches = 0
        for i in range(len(list_set_1)):
            for j in range(len(list_set_2)):
                if list_set_1[i] == list_set_2[j]:
                    count_of_matches += 1
                    break
        if count_of_matches == len(list_set_1):
            return f'Наборы равны.'
        else:
            return f'Супермножество не обнаружено.'



    
list_set_1 = [1, 3, 5, 7]
list_set_2 = [3, 5]
list_set_3 = [5, 3, 7, 1]
list_set_4 = [5, 6]

print(list_superset(list_set_1, list_set_2))
print(list_superset(list_set_2, list_set_3))
print(list_superset(list_set_1, list_set_3))
print(list_superset(list_set_2, list_set_4))
