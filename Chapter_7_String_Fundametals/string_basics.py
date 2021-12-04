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