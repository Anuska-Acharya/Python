"""
Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')
"""
n=input("Enter a sequence of comma-separated numbers: ")
list_1=n.split(",")
tuple_1=tuple(list_1)
print(list_1)
print(tuple_1)
