'''
String Special Operators
       0 1 2 3 4 # Left to Right index
       -5 -4 -3 -2 -1 # Right to Left index
Assume string variable a holds 'Hello' and variable b holds 'python', then :

'''

# Creating of String Variables in Python

a = 'Hello'

b = 'Python'

a + b
# Accessing Variables in Python

print ("String concatenate +" + a + b)

print("Accessing a Variable i.e. a : ", a[0])

print(" ")

print("Accessing a Variable i.e. a : ", a[4])

print("Left TO Right Index i.e. a : " , a[1])

print("")

print("Right to left index i.e. a : ", a[-4])


print("Left TO Right Index i.e. a : " , a[0:5])

print("")

print("Right to left index i.e. a : ", a[0:2])


print(r'\n')

# Error print('\n')

# print(\n)

print(r'c:\\Users\\deepthi')


print("My name is %s and I born in %d" % ('Python', 1981))

var1='Python'
var2=1981

print("My name is %s and I born in %d" % (var1, var2))


var3 = "Amar"
var4 = 1980

print("My name is {} and I born in {}".format('Guido van Rossum',1981))


print("")

print ("My name is {} and I born in {}".format(var3,var4))


print("My name is {var3} and I born in {var4}".format(var3='python',var4=1969))


print("My name is {0} and I born in {1}".format(var3,var4))

firstname='Guido'
lastname='Rossum'

FullName = firstname[0] + " & " + lastname[0]

print(FullName)

print(firstname*5)


#01234567891011

#-11-10-9-8-7-6-5-4-3-2-1

strx= 'Hello World!'   # 11 characters

stry = 'This is an example string'

alphabets='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print (strx[0])

print(strx[-1])

print (strx[2:6])

print(strx[:5])

print(strx * 3)


print(alphabets[0::5])  # Zero Based Indexing

print ("updated string ", strx[:6] + "planet")

print ("updated string ", strx[:12] + "perl")


# formating of strings

print ("your name is %s and your account id is %d"  %("kevin", 14456))

print("Calling strx {0} and calling stry {1}".format(strx,stry))












