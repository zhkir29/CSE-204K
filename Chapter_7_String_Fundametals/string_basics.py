#in the text department ,this includes symbols and words (e.g.youre name) ,contents of text files loaded in to memory ,internet addresses ,python source code and so on.
# Python strings are categorized as immutable sequence ,meanig that the characters they contains have left to right positional order and that the cannot be changed in place.
#String supports Contcatenatioin , slicing ,indexing ,

#implicit concatenation
title="Meaning " 'of' " Life"
print(title)

#Adding commas between them these strings would result in a tuple ,not a string.
s='Knight\'s',"knight\"s"
print(s)

#backslashes are used to introduce special character conding known as escape sequence.
s= 'a\nb\tc'
print(s)
print(len(s))
#raw strings:
print(r"C:\new\test.spm")

print("This is \newline character")
print("This is \\ backslash character")
print("This is \'single \'quotes")
print("This is \"double quotes\"")
print("This \b is for bell\a ")
print("This is for \f formfeed")
print("This is for \r carriage return")
print("This is \t for horizontal tab")
print("This is for \v vertical tab")
print("\x91 hexadecimal value of the character")

