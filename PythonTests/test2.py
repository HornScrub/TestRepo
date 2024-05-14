import random


'''

print("Hisss...")
print("Hello world!")

print()
print("Anthony")

print("The dog ran across the street.\nHe was chasing a car.")

print("My name is", "Python.  ", end="%")
print("Monty Python.")

print("My", "dog", "is", "handsome", "!", sep=' ', end=':)')

'''
'''

print("2")
print(int(2))
name = int(43)
print(name)
print(str(name))

'''

'''
print(2 * 3)
print(2 ** 3)
print(type(6 / 3))
print(type(7 // 3))
'''

'''
num = 3
name = "Ben"

print("My name is ", name, "!", sep='')
print(f"My name is {name}!")
'''


# print(round(8.234 * 9.4253, 2))

# print(1==2)

i = 0

range = []
range2 = ()

range = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range:
    print(i)

#For, While, Do-While

#For - You know how many times you want the loop to iterate
#While - You want the loop to iterate for as long as some condition is being met
#DoWhile - You want to iterate at least once, and then iterate for as long as some condition is being met

'''
range3 = []
max = 1000
i = 0

while i <= max:
    range3.append(i)
    i += 1
    

for i in range3:
    if ((i % 3) == 0):
        print(i, end=' ')
'''

'''
aDict = {}

i = 0
while i < 5:
    aDict[random.randint(1000, 9999)] = random.randint(0,99)
    i += 1

print(aDict)
'''

bob = "34"


print("Enter a number: ", end='')
num = int(input())

print(num)

f = open("/home/ben/Desktop/TestRepo/demofile.txt", "w")

print("Enter some text: ", end='')
text = input()
f.write(text)
f.close()
