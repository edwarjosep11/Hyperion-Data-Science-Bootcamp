# Sentence: The!quick!brown!fox!jumps!over!the!lazy!dog!

# Declaring varible
string = 'The!quick!brown!fox!jumps!over!the!lazy!dog!'
# Replacing the "!" with blank spaces and rewriting it
string = string.replace('!',' ').upper()
# Printing the reversed string
print(string[::-1])
