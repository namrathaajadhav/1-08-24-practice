#functions

def person_details(name, age,city="Hyderabad"):
    print("name",name)
    print("age",age)
    print("city",city)
person_details("rohu",50)
person_details('sonu',"Hyderabad")

def greet(name, greeting="Hello"):
  print(greeting, name)
greet("rose")
greet("lilly", "Hi")

#position arguments
numbers = [1,2,3,4,5]
total =sum(numbers)
print(total)

numbers = [1,2,3]
total =sum(numbers, start=10)
print(total)

#key word argument 

def greet(name, greeting="Hello"):
    print(greeting, name)
greet(name="namratha",greeting="Hi")

#default argument
def subjects(maths=65,social=75,science=80,english=98):
   return{"maths":maths,"social":social,"science":science,"english":english}
result=subjects()
print(result)


#variable length
def add_numbers(x,y,z):
   return x+y+z
numbers=[1,2,4]
result= add_numbers(*numbers)
print(result)