arr = [61, 228, 9]

str_arr = [str(x) for x in arr]

number = int(''.join(sorted(str_arr, key=lambda x: x[0], reverse=True)))

print(number)