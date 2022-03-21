# numbers 1 thru 9
x = [i for i in range(10)]
print(x)

# adding an expression - square each number
squares = [i**2 for i in range (10)]
print(squares)

# multiply each element by 3

list1 = [3,4,5]
multiplied = [item*3 for item in list1]
print(multiplied)

# word manipulation

listofwords = ["this","is","a","list","of","words"]
fl = [word[0] for word in listofwords]
print(fl)

list1 = ['A','B','C']
lc = [x.lower() for x in list1]
print(lc)

#IF condition

new_range = [i for i in range(5) if i%2 ==0]
print(new_range)


string = "Hello 12345 World"
numbers =[n for n in string if n.isdigit()]
letters = [w for w in string if w.isalpha()]
print(numbers)
print(letters)

#using a file
myfile = open('test.txt','r')
result = [i.rstrip("\n") for i in myfile if "line 3" in i]
print(result)

#using functions
def double(x):
    return x*2

print(double(10))

#for even numbers
mynumbers = [double(x) for x in range(10) if x%2 == 0]
print(mynumbers)


# more than one argument
result = [x+y for x in [10,30,50] for y in [20,40,60]]

print(result)