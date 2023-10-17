def merge_sorted_lists(list1, list2):
    result = []
    list1_index = 0
    list2_index = 0
    last_added_item = float("-inf")

    for i in range(len(list1) + len(list2)):
        if list2_index == len(list2) or (list1_index < len(list1) and list1[list1_index] < list2[list2_index]):
            if list1[list1_index] != last_added_item:
                result.append(list1[list1_index])
                last_added_item = list1[list1_index]
            list1_index += 1
        else:
            if list2[list2_index] != last_added_item:
                result.append(list2[list2_index])
                last_added_item = list2[list2_index]
            list2_index += 1
    return result


l1 = [5, 5, 6, 7, 8]
l2 = [5, 5, 6, 9, 10, 11, 12]

merged = merge_sorted_lists(l1, l2)
print(merged)
