#A list is a collection which is ordered and changable.Allows duplicate. 

#Create a list, it is a way to do it
numbers = [1, 2, 3, 4, 5]
fruits = ["Apples", "Orange", "Grapes", "Pears"]
 
#create a list ussing constructor

numbers2 = list((1, 2, 3, 4, 5))
print(numbers, numbers2)

#Get a value of the list 

print(fruits[0])

#Get length

print(len(fruits))

#Append to the list 

fruits.append("Mangos")
print(fruits)

#Remove from the list 

fruits.remove("Grapes")
print(fruits)

#Insert to position 

fruits.insert(2,"strawberries")
print(fruits)

#Remove from the position whith pop 

fruits.pop(2)
print(fruits)

#Reverse the list 

fruits.reverse()
print(fruits)

#sort alphabetically 

fruits.sort()
print(fruits)

#staroverflow es la página para buscar informacion a cerca de python 
