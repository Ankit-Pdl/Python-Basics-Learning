# for loop

# fruits = ['a','b','k']

# for fruit in fruits:
#   print(fruit)

# range function

# for i in range(1,6):
#   print(i)

# while loop

# count =1
# while count<=5:
#   print(count)
#   count += 1

# loop control statement

# for letter in "Anamika":
#   if letter  == 'k':
#     break
#   print(letter)



# for i in range(1,6):
#   if i == 4:
#     continue
#   print(i)

# for item in ['A','B','C']:
#   if item == 'B':
#     pass
#   else:
#     print(item)

# for i in range (1,11):
#    print(f'34 * {i}: {i*34}')


# N = int(input("enter a num\t"))
# N+=1
# sum = 0
# for i  in range(N):
#    sum += i


# print(sum)

# string = 'anamika'
# for i  in string:
#   print(i)

# count = 0
# string = 'anamihdjfbweifnaksaJBWJSDCQBFAAAADV'
# for i in string.lower():
#   if i == 'a':
#     count +=1

# print(count)

# for i in range(1,101):
#   if i%3 == 0 and i%5 ==0:
#     print(i)
# result  = []
# for i in 'ankit':
#    result.insert(0,i);
# print(result)

# s= 'yunisha'
# rev = ''

# for ch in s:
#   rev = ch +rev

# print(rev)

# lists = [1,2,3,4,5]
# max = list[0]
# for items in list:
#    if items> max:
#       max_num = items

# print(max_num)

# print(max(lists))

# count =0
# num = 12345
# for i in str(num):
#   count+=1

# print(count)  
 

# num = 343754343433
# count = 0

# while num!=0:
#   num = num //10
#   count+=1
# print(count)  

# n = int(input("num: "))
# result  = 1
# while n>1:
#   result = result * n
#   n = n-1
  
# print(result)  


# def factorial(n:int)-> int:
#   """Return fact of a non negative number: """
#   if n<0:
#     raise ValueError("Facotrial is not defined for negative numbers: ")
#   result  =1
#   for i in range(1,n+1):
#     result *= i

#   return result

# if __name__ =="__main__":
#   num = int(input("Enter a nunber:"))
#   print("factorial",factorial(num))  


# for i in range(1,6):
#   for j in range(1,i+1):
#     print("*",end="")
#   print()  

# for i in range(1,6):
#   for j in range(1,i+1):
#     print(j,end="")
#   print()

# hard level
# import math

# n = int(input("enter a number: "))

# if n<=1:
#   print(f'{n} is neither prime nor composite')
# else:
#   is_Prime =True
#   for i in range(2,int(math.sqrt(n))+1):
#     if n%i ==0:
#       is_Prime=False
#       break
#   print(f"{n} is a prime number " if is_Prime else f"{n} is a composite number" )  

# import math
# n = int(input("enter a number: "))
# if n<=1:
#   print(f'{n} is neither')
# else:
#   is_Prime = True
#   for i in range(2,int(math.sqrt(n))+1):
#    if n% i ==0:  
#      is_Prime= False
#      break
#   print(f'{n} is a prime number' if is_Prime else f'{n} is a composite') 
# program to print all the prime numbers between 1 and 100