print(0o1,0o20,0o377) # octal literals:base-8 ,digits 0-7(3.X,2,6+)
print(0x1,0x10,0xFF)  # Hex literals:base-16 ,digits 0-9/A-F (3.X ,2.X)
print(0b1,0b10000,0b11111111) #Binary literals: base-2,digits 0-1;(3.0X ,2.6+)

print(oct(64),bin(64),hex(64))

print(int('100',8),int('1000000',2))

# you can also convert intergers to base specific strigs with 'string formatting' method calls and expressions ,which returns just digits ,not 
# python literal strings 
print('{0:o},{1:b},{2:X}'.format(64,64,64))
print('%o,%x,%x,%x'%(64,64,255,255))