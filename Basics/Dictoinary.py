# dictionary vaneko set of data ho 

# student = {
#   "name": "Anamika",
#   "age":21,
#   "faculty": "CSIT",
#   "University": "Tribubhan University"

# }
# # print(student["name"])

# # creating dictionaryy:
# data ={}

# person = dict(name = "Unsaa",age= 19)
# users = {
#   1:{
#     "name":"Ankit", "age":21
#   },
#   2:{
#     "name":"Yunisha","age":19
#   }
# }

# accessing

# print(users[2])

# person["name"]= "Ankit"
# print(person["name"])

# # person.clear()
# print(person["name"])
# users["AP"]={"name":"Samriddhi"}
# print(users["AP"])

# # users.pop("AP")
# print(users["AP"])


# iterations

student ={
  "name":"Ankit",
  "age":21,
  "address":"Sanothimi "
}

# for key,value in student.items():
#   print(f'{key}: {value}')

#dictionary methods

# print(student.keys())
# print(student.values())
# print(student.items())


# nested dictionaries

# employess = {
#   "emp1":{"name":"Anamika","salary":340666},
#   "emp2":{"name":"Abhjit","salary":235685},
# }

# print(employess["emp1"]["salary"])
#dictionary comprehensation

# square = {x:x**2 for x in range(1,7) if x%2 ==1}
# print(square)

# word = "abdjdbd;fdjdovbsdvb"
# freq = {}
# for ch in word:
#   freq[ch]= freq.get(ch,0)+1
# print(freq)  

# sentence = "Hello I am i World am I form the world"
# freq = {}
# sentence = sentence.lower()

# temp =sentence.split()
# for ch in temp:
#   freq[ch] = freq.get(ch,0)+1

# print(freq)

# program to store the marks of 5 students and find the topper

students= {}

for i in range(1,3):

  userName = input("Enter the name of the student ")
  try:
    marks = float(input("Enter the student's overall marks in 100: "))
    if not 0<=marks<=100:
     raise ValueError("Number cannot be greater than 100")
  except ValueError as e:
    print("Input error",e)
  
  students[f'{i}']= {"name":userName.lower().capitalize(),"marks": marks}
  


topper = max(students.values(), key=lambda x: x["marks"])

print("Topper: ", topper["name"])
print("Marks: ",topper["marks"])