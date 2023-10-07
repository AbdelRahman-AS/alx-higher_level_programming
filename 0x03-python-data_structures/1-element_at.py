#!/usr/bin/python3
def element_at(my_list, idx):
    length = len(my_list)
    if idx > length or idx < 0:
<<<<<<< HEAD
        return "None"
=======
        return None
>>>>>>> d39fd9f82871bfe60d2c0f211f2eb231cfa25eb4
    for i in range(0, length):
        if i == idx:
            return my_list[i]
