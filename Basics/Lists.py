#creating lists

# numbers = [1, 2, 3, 4, 5]
# mixed_list = [1, "Hello", 3.14, True]
# empty_list = []
# print(f'{type(numbers)}: {numbers} \n {type(mixed_list)}: {mixed_list} \n {type(empty_list)}: {empty_list}')



#accessing list elements

# print(numbers[-5])

#slicing
# print(numbers[1:4])
# print(numbers[:3])
# print(numbers[3:])
# print(numbers[::3])

# changing items
# a[1] = 2
# print(a)

# adding items ( function used = append())

# a.append (4)  last ko lagi yo hunxa

# print(a)

# insert()

# a.insert(3,23)
# print(a)

# a = [1,2,3]
# a.extend([5,6])
# print(a)


# removing items
# print(f'previous value of list {a}')
# a.remove(23)
# print(f'after removal: {a}')
# a.pop(3)
# print(f'initial list: {a}')
# a.clear()
# a= [1,2,3,4,5]

# # list operations
# b= [1,2]+[3,4]
# b= [1]*10
# print(b)

# print(a)

# a = [2,3,4,5,6,7,8,9]
# for i in range(len(a)):
#  print(i,a[i])

#enumerate()
# a= [1,2,3,4,5]
# for index, value in enumerate(a):
#   print(index,value)


# list comprehensation.



# squares = [num*num for num in numbers]
# even_items = [num for num in numbers if num%2==0]
# print(squares)
# print(even_items)

# categorized_nums =["even"if num%2 ==0 else "odd" for num in numbers]
# print(categorized_nums)

# even = [x for x in range(101)if x%2==0]
# print(even)
# numbers = [2,3,1,4,6]
# print(f'initial list: {numbers}')
# new = sorted(numbers)
# reversed = sorted(numbers, reverse=True)
# print(f'sorted list:{new} \n reversed_sorted: {reversed}')


#nested lits

# matrix = [
#   [1,2,3],
#   [4,5,6]
# ]
# print(matrix[0][1])

# num = [1,2,3]
# print(len(num))
# print(sum(num))
# print(max(num))
# print(min(num))

# difference between append and extend

#copying a list

# a= [1,2,3]
# b=a
# b[0]=5
# print(a)
# a=[1,2,3]
# b= a.copy()
# b[0] =5
# print(a)
# print(b)

# import copy
# a = [
#   [1,2,3],
#   [4,5,6]
# ]
# # b= a.copy()
# # b[1][1] = 54
# # print(a)

# b= copy.deepcopy(a)
# b[0][0]= 99
# print(b)


# QUESTION TIME

# sum of all numbers

# a=[5,10,15,20]
# print(sum(a))

# largest number in a list
# a =[ 3,9,2,5,7]
# print(max(a))


# a = [1,2,2,3,4,2,5]
# # # count_2 = a.count(2)
# # # print(count_2)

# # a= [x for x in a if x!=2]
# # print(a)
# b = a.copy()
# b.sort()
# print(b)
# reversed = b[::-1]
# print(reversed)


# a = [1,2,3,4,5,6,7,8]
# even = [x for x  in a if x%2==0]
# print(even)

# Create a list of squares from 1 to 10 using list comprehension

# output = [x*x for x in range(11) ]
# print(output)

# a = [10,20,4,45,99]
# a.sort()
# print(f'second largest in list:{a[3]}')

# a = [[1,2],[3,4],[5,6]]
# flattend = [x for sublist in a for x in sublist]
# print(flattend)

# a = [1,2,2,3,4,4,4,5]
# # b= set(a)
# # b= list(b)
# # print(b)

# a = list(dict.fromkeys(a))
# print(a)