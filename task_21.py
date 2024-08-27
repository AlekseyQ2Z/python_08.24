list_dict = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}] 
new_list = list()
for dictionary in list_dict:
    for key, value in dictionary.items():
        if value not in new_list:
            new_list.append(value)
print(new_list)

