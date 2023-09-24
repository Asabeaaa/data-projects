# Input array   =  [0, 1, 0, 1, 0, 0, 1, 1, 1, 0]
# Output array =  [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]

def segregate_nums(num_list):
    # zero_list = []
    # one_list = []
    final_list = []
    left_index = 0
    right_index = len(num_list) - 1

    for num in num_list:
        if num == 1:
            final_list[left_index] = num
            left_index += 1

        elif num == 0:
            final_list[right_index] = num
            right_index -= 1

    # [one_list.append(num) if num == 1 else zero_list.append(
    #     num) if num == 0 else 'num not one or zero' for num in num_list]

    # final_list = zero_list + one_list
    return final_list


print(segregate_nums([0, 1, 0, 0, 0, 0, 0, 1, 0, 0]))
