s = input("Enter a word: ")
c = s[0]
str1 = s[1:].replace(c, '$')  # Replace only in the rest of the string
print(c + str1)
