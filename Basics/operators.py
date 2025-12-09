# aru tha xa
# exponenetiation 

# x=3
# y=4
# print(x**y)

# def power(base, exponent):
#     return base** exponent

# print(power(2,9))  # 512
    
# x=13
# y=3
# print(x//y)

# x= 5
# # print(x|3)

# print(x)

# x<<= 3
# print(x)
# warlus operation

# numbers = [1,2,3,4,5]
# count = len(numbers)
# if count>3:
#   print(f'List has the {count} elements')
# if(count:= len(numbers))>3:
#   print(f'list has {count} elements')  

# line =  input()
# while line!="":
#   print(line)
#   line = input()

# while(line := input())!='':
#   print(line)

# nums = [1,2,3,4,5]
# squared = [y for x in nums if (y:=x**2)>0]
# print(squared)

# x=4
# y=5
# if x==y:
#   print('same')
# else:
#    (print('not same'))  


# x= 5
# print(not(x>0 and x%2==0))

#identity operator 

#identity operators

# x=2
# y=2

# print(x is not y)

# num = [1,2,3,4,5,6,7]
# print(1 in num)

# string = 'anamika'

# print('a' in string)
# print('Anamika' in string)
# print('z' not in string)

# x= 7
# print(x<<2)
# even_sum = 0
# for x in range(101):
#   if x%2==0:
#    even_sum+= x

# print(even_sum)

# vowel_count = 0

# string= input('enter any string ')
# for x in string:
#   if (x=='a' or x=='e' or x=='i' or x=='o' or x=='u'):
#     vowel_count+=1

# print(f'the vowel count in your string is: {vowel_count}')



# string = input('enter any string ')
# vowels = sum( 1 for x in string if x.lower() in 'aeiou')
# print('Vowel Count', vowels)

# largest of 3 numbers
# user_input = []
# i = 1
# while i<=3:
#   user_input.append(int(input('enter any integer')))
#   i+=1

# print(f'maxiumum in your list is {max(user_input)}')


# numbers = [int(input("Enter a number: ")) for _ in range(3)]
# print("Maximum is", max(numbers))


# numbers = [int(input('Enter an integer: ')) for _ in range(3)]
# print("Maximum is ", max(numbers))




# filtered_list = [x for x in nums if x>=10]
# print(filtered_list)


# filtered_list = [y for x in nums if (y:=x)>10]
# print(filtered_list)

# program to remove dublicates.
# nums  = [1,5,10,15,20,5,7,20,7,1,15]
# # new_data = set(nums)
# # print(list(new_data))

# new_data = []
# for num in nums:
#   if num not in new_data:
#     new_data.append(num)
# print(new_data)    

# userInput = int(input("Enter any number: "))
# if userInput &1:
#   print("odd")
# else:
#   print('even')  

# n = int(input("enter a number\t"))
# result = []

# for x in range(1,n+1):
#   result.append(x**2)

# print(result)

# n = int(input("enter a number: "))

# result = [x**2 for x in range(1,n+1)]
# print(result)

# print([x**2 for x in range(1,int(input("Enter a number: "))+1)])

# n = int(input("enter a number: "))
# print(*(x**2 for x in range(1,n+1)))


# program to reverse a list

# my_list = [1,2,3,4,5,3,5,67,5,4,6]

# reversed= my_list[::-1]
# print(reversed)

# password = input("enter any string ")

# length_ok = len(password)>=8

# has_number = any(char.isdigit() for char in password)

# has_upper = any(char.isupper() for char in password)

# if length_ok and has_number and has_upper:
#   print('strong password')
# else:
#   print('weak password') 

# print('number will be added until first negative number provided:\n')
# total = 0
# while(num:=float(input("Enter any number: ")))>=0:
#   total+=num
# print("Sum:",total)




