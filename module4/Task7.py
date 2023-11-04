nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

result = [third_depth for first_depth in nice_list for second_depth in first_depth for third_depth in second_depth]

print(result)
