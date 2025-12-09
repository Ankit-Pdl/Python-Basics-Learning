# multilined strings

# name = """Ankit is a legend
# in his own mind."""

# print(name)


# s = 'anamika'
# print(s[3])


#slicing

# s[start:end:step]

# name = 'Sunderland'
# print(name[0:3])
# print(name[:5])
# print(name[3:])
# print(name[0:6:2])

# name = 'Sunderland'
# surname = 'Nepal'
# print(name+" "+surname)
# print("yunisha\n"*5)

# name = 'yunisha'
# print("sHa" in name)

# # name = 'Yunisha Poudel'
# # for ch in name:
# #   print(ch)  iteration

# name = 'yunIsha Poudel is a good girl'

# # print(name.lower())
# print(name.upper())
# print(name.title())
# print(name.capitalize())

# print(name.count('a'))
# temp_name = name.replace('a', 'i')
# print(temp_name)

# print(name.startswith('yun'))
# print(name.endswith('irl'))

# name = 'hello world'.split()
# print(name)
# print(type(name))

# string = 'Anamika is not a good girl'
# print(string.split(' '))

# name = '.'.join(['Ankit','Poudel'])
# print(name)


# string = ' hello from the other sideee '
# print(string.strip())

# print(string.lstrip())

# string = 'Nepal'
# print(string.isalpha())
# print(string.isdigit())
# print(string.isalnum())
# print(string.islower())
# print(string.isupper())

# name = 'Anamika'
# age= 22
# print(f'my name is {name} and I am {'twenty-one' if age==21 else 'dont know'} years old')


# print(ord('A'))
# print(chr(126))


# import time
# from strings import text
# for char in text:
#   print(char,end="", flush=True)
#   time.sleep(0.09)

# name = 'hello'
# print(name[::-1])
# reversed_string = ''
# name = 'hello from the other side'
# for char in name:
#   reversed_string = char + reversed_string
# print(reversed_string)  
# empty = []
# ascii=''
# from strings import text
# count = 0
# vowels = 'aeiouAEIOU'
# # user_Input = input("enter any string ")
# for char in text:
#   if char in vowels:
#     ascii = ord(char)
#     empty.append(ascii)

# result = list(set(empty))
# result.sort()

# print(result)

# from strings import text
# vowels = 'aeiouAEIOU'
# ascii_values = sorted({ord(char) for char in text if char in vowels})
# print(ascii_values)

# string = input("enter a string ")
# result = string.replace(' ', '')
# print(result)

# find the most frequent character in a string

# text = input("Enter a string:")
# freq = {}
# print(type(freq))
# for char in text:
#   freq[char] = freq.get(char, 0)+1

# most_frequent = max(freq,key=freq.get)
# print("Most frequent character: ", most_frequent)
# print("Frequency: ",freq[most_frequent])


# def most_frequent_char_max(s):
#     # Iterate over unique characters to avoid redundant counting
#     if not s:
#         return None, 0
        
#     most_common_char = max(set(s), key=s.count)
#     frequency = s.count(most_common_char)
#     return most_common_char, frequency

# # Example Usage:
# input_string = "speed demon"
# char, count = most_frequent_char_max(input_string)
# print(f"The most frequent character is '{char}' with a count of {count}.")
