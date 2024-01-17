numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
ind_none = 4
sum_numbers = sum(numbers[:ind_none]) + sum(numbers[ind_none+1:])
count_numbers = len(numbers)
average = sum_numbers / count_numbers
numbers[ind_none] = average
print("Измененный список:", numbers)
