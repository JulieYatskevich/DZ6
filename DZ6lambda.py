even_list = [1,3,5,7,9,11,13]
odd_list = [2,4,6,8,10,12,14]

sum_list = list(map(lambda x,y: x*y, even_list, odd_list))
print(sum_list)

fil_numbers = list(filter(lambda x: x >= 56, sum_list))
print(fil_numbers)


from functools import reduce
sum_numbers = reduce(lambda x,y: x+y, fil_numbers)
print(sum_numbers)