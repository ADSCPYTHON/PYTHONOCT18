var1= "this2020"

print(var1.isalnum())


var2 = "Python world .....wow!!!"

print(var2.isalnum())

print(var2.isalpha())


str1  = "this"  # No space & digit in this string

print(str1.isalpha())

str2 = "Python and perl......linux!!!!"

print(str2.isalpha())


_007 = u"$6"

print (_007.isnumeric())

_008 = u"786786"

print (_008.isnumeric())

_009 = "786786"

print(_009.isnumeric())


_0099 = "03948274"  # only digit in this string

print(_0099.isdigit())

_0066 = "Linux Unix Perl Python and django...etc!!! 0066"

print(_0066.isdigit())



str4 = "44"

print (str4.isdecimal())

str5 = u"695979"

print(str5.isdecimal())

print("Amar this is isdecimal isdigit isnumeric methods testing")

#c = "\u0123456789"  # decimal - radix numbers

#C = '\u2155'

C = '\u214675'

#C = r'\u2155'

#C = u"77"

#C = "77"

#c = u'77' # 0-9


print(C)
print(C.isnumeric())
print(C.isdecimal())
print(C.isdigit())


_01_ = '   '

print(_01_.isspace())

_02_ = "Linux Unix"

print(_02_.isspace())

_03_ = "Linux Unix Perl Python and django...etc!!!"

print(_03_.isspace())

"""
is space()
Returns true if string contains only white space
characters and false otherwise.
"""

"""

istitle()
returns true if string is properly "titlecased"
and flase otherwise.
"""

_Iphone7 = "Linux Unix Perl Python And Django...Etc!!!"

print(_Iphone7.istitle())

_Iphone8 = "Linux unix perl Python And Django...Etc!!!"

print(_Iphone8.istitle())


print("Amar Method rfind")

str6 = "this is is abc is really a string example....wow!!!"
str7 = "is"


print(str6.rfind(str7, 0, 10))







"""

14 isnumeric()
   Returns true if a unicode string contains only numeric
   characters and false otherwise. 

"""




