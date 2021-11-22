#Discussion about python numeric types and their operations.
# A complete inventory of pythons numeric toolbox includes: 1.Interger and floating point objects 2.Complex number objects 3.Decimal: Fixed precision objects
#page -143:
a=3
b=4
print(b/(2+a))



num=1/3.0
print(num) # print explicitly


print('%e' % num) #string formatting expression
print('%4.2f' % num) #alternative floating point foramt

print('{0:4.2f}'.format(num)) # string formatting method :python 2.6 ,3.0 and later

# str and repr display formats

# The difference between default interactive echoes and print corresponds to the difference between the built in repr and str functions.
repr("spam") # used by echoes:as-code form
str("spam") # used by print :user friendly forms